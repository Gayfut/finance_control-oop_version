import json
from datetime import datetime
import settings


class ArticleJSONManager:
    """CRUD for article in JSON file"""

    def __init__(self):
        self.article_list = []

    def add_article_in_list(self, article_dict):
        self.article_list = self.get_article_list()
        self.article_list.append(article_dict)

    def write_article_list(self):
        for _article in self.article_list:
            _article["date_create"] = _article["date_create"].strftime(
                settings.DATE_FORMAT
            )

        with open("article_list.json", "w", encoding="utf-8") as file_with_article:
            json.dump(self.article_list, file_with_article, ensure_ascii=False)

    def get_article_list(self):
        try:
            with open("article_list.json", encoding="utf-8") as file_with_article:
                self.article_list = json.load(file_with_article)
        except FileNotFoundError:
            self.article_list = []

        for _article in self.article_list:
            _article["date_create"] = datetime.strptime(
                _article["date_create"], settings.DATE_FORMAT
            ).date()

        return self.article_list
