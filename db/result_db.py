from db import article_db
from settings import ARTICLE_INCOME, ARTICLE_OUTLAY


class ResultManager:
    @staticmethod
    def get_income_result():
        article_list = article_db.ArticleBufferedJSONManager.get_articles()
        income_result = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_INCOME:
                income_result += _article.amount

        return income_result

    @staticmethod
    def get_outlay_result():
        article_list = article_db.ArticleBufferedJSONManager.get_articles()
        outlay_result = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_INCOME:
                outlay_result += _article.amount

        return outlay_result

    @staticmethod
    def get_final_result():
        article_list = article_db.ArticleBufferedJSONManager.get_articles()
        final_result = 0
        amount = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_OUTLAY:
                amount = -(_article.amount)
            else:
                amount = _article.amount
            final_result += amount

        return final_result
