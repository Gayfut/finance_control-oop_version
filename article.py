"""file for control base article"""
from datetime import datetime


class Article:
    """control article specification"""

    def __init__(
        self, name, amount, article_type, category, date_create=None, article_id=None
    ):
        """create article"""
        self.name = name
        self.amount = amount
        self.article_type = article_type
        if date_create is None:
            self.date_create = datetime.today()
        else:
            self.date_create = date_create
        self.category = category
        if article_id is None:
            self.article_id = "id" + str(id(self))
        else:
            self.article_id = article_id

    def to_dict(self):
        """return article in dict format"""
        article_dict = {
            "name": self.name,
            "amount": self.amount,
            "article_type": self.article_type,
            "date_create": self.date_create,
            "category": self.category,
            "id": self.article_id,
        }

        return article_dict
