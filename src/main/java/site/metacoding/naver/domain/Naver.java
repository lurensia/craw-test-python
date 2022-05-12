package site.metacoding.naver.domain;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Document(collection = "navers") // greendb/navers
public class Naver {
    @Id
    private String _id;
    private String company;
    private String title;
    private String createdAt;
}
