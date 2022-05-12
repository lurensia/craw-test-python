import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType

list = []
dictresult = {}
dictlist = []


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


mongo = MongoClient("localhost", 20000)

id = "1"
while True:
    print("id --> "+id)
    aid = id.zfill(10)
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
        # print(html.status_code)
        # print(html.status_code)
        if(html.status_code == 500):
            pass

        if(html.status_code == 200):
            try:
                soup = BeautifulSoup(html.text, "html.parser")
                title = soup.select_one(".media_end_head_headline").text
                createdAt = soup.select_one(
                    ".media_end_head_info_datestamp_time").text
                conpany = soup.select_one(
                    ".media_end_head_top_logo_img")
                # print(title)
                # print(createdAt)
                # print(conpany["alt"])

                list.append(title)
                list.append(createdAt)
                list.append(conpany["alt"])

                dictresult = dict(
                    company=conpany["alt"],
                    title=title,
                    createdAt=createdAt)
                # print(dictresult)
                dictlist.append(dictresult)

            except Exception as x:
                pass

        if len(list) == 60:
            # print(list)
            break

        id = str(int(id) + 1)
    except Exception as e:
        pass

# print(dictlist)
mongo_save(mongo, dictlist, "greendb", "navers")
