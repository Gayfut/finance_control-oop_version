import json
from datetime import datetime
from article import Article
import settings


class ArticleBufferedJSONManager:
    """CRUD for article in JSON file"""

    ARTICLE_BUFFER_SIZE = 5

    def __init__(self, buffer_size=None):
        if buffer_size is None:
            self.__buffer_size = self.ARTICLE_BUFFER_SIZE
        else:
            self.__buffer_size = buffer_size
        self.__article_buffer = []

    def flush_articles(self):
        article_list_for_save = []
        for _article in self.__article_buffer:
            _article_dict = _article.to_dict()
            _article_dict["date_create"] = _article_dict["date_create"].strftime(
                settings.DATE_FORMAT
            )
            article_list_for_save.append(_article_dict)

        with open("article_list.json", "w", encoding="utf-8") as file_with_article:
            json.dump(article_list_for_save, file_with_article, ensure_ascii=False)

    def save_article(self, article):
        self.save_articles([article])

    def save_articles(self, article_list):
        self.__article_buffer.extend(article_list)

        if len(self.__article_buffer) <= self.__buffer_size:
            return

        self.flush_articles()

    @staticmethod
    def get_articles():
        article_list = []
        try:
            with open("article_list.json", encoding="utf-8") as file_with_article:
                article_list_with_dicts = json.load(file_with_article)
        except FileNotFoundError:
            return article_list

        for article_dict in article_list_with_dicts:
            article_dict["date_create"] = datetime.strptime(
                article_dict["date_create"], settings.DATE_FORMAT
            ).date()

            article = Article(
                article_dict["name"],
                article_dict["amount"],
                article_dict["article_type"],
                article_dict["category"],
                article_dict["date_create"],
            )
            article_list.append(article)
        return article_list
