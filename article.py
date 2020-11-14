from datetime import datetime
# from db import article_db


# class ArticleList:
#     """control article list"""
#
#     def __init__(self):
#         self.article_manager = article_db.ArticleJSONManager()
#         self.article_list = self.article_manager.get_article_list()
#
#     def add_article_in_list(self, article_dict):
#         self.article_list.append(article_dict)
#
#     def get_article_list(self):
#         return self.article_list


class Article:
    """control article specification"""

    def __init__(self, name, amount, article_type, category):
        self.name = name
        self.amount = amount
        self.article_type = article_type
        self.date_create = datetime.today()
        self.category = category

        self.article_dict = None

    def to_dict(self):
        """return article in dict format"""
        self.article_dict = {
            "name": self.name,
            "amount": self.amount,
            "article_type": self.article_type,
            "date_create": self.date_create,
            "category": self.category,
        }

        return self.article_dict
