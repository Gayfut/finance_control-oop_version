from datetime import datetime
from settings import ARTICLE_INCOME, ARTICLE_OUTLAY


class Article:
    """control article specification"""

    def __init__(self, name, amount, article_type, category, date_create=None):
        """create article"""
        self.name = name
        self.amount = amount
        self.article_type = article_type
        if date_create is None:
            self.date_create = datetime.today()
        else:
            self.date_create = date_create
        self.category = category

    def to_dict(self):
        """return article in dict format"""
        article_dict = {
            "name": self.name,
            "amount": self.amount,
            "article_type": self.article_type,
            "date_create": self.date_create,
            "category": self.category,
        }

        return article_dict


class IncomeArticle(Article):
    """control income article specifications"""

    def __init__(self, name, amount, category):
        super().__init__(name, amount, ARTICLE_INCOME, category)


class OutlayArticle(Article):
    """control outlay article specifications"""

    def __init__(self, name, amount, category):
        super().__init__(name, amount, ARTICLE_OUTLAY, category)
