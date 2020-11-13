import json
from copy import deepcopy
from datetime import datetime
import settings


class JSONArticle:
    """CRUD for article in JSON file"""

    def __init__(self):
        self.article_list = []

    def write_article_list(self, article_list):
        for _article in article_list:
            _article["date_create"] = _article["date_create"].strftime(
                settings.DATE_FORMAT
            )

        with open("article_list.json", "w", encoding="utf-8") as file_with_article:
            json.dump(article_list, file_with_article, ensure_ascii=False)

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
