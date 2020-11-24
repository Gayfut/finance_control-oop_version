"""file for control income article"""
from article import Article
from settings import ARTICLE_INCOME


class IncomeArticle(Article):
    """control income article specifications"""

    def __init__(self, name, amount, category, date_create=None):
        super().__init__(
            name, amount, ARTICLE_INCOME, category, date_create=date_create
        )
