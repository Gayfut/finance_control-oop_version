"""file for control outlay article"""
from article import Article
from settings import ARTICLE_OUTLAY


class OutlayArticle(Article):
    """control outlay article specifications"""

    def __init__(self, name, amount, category, date_create=None):
        super().__init__(
            name, amount, ARTICLE_OUTLAY, category, date_create=date_create
        )
