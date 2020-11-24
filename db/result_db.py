"""file for result DB control"""
from settings import ARTICLE_INCOME, ARTICLE_OUTLAY


class ResultManager:
    """control methods for different results"""

    @staticmethod
    def get_income_result(article_list):
        """return income result"""
        income_result = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_INCOME:
                income_result += _article.amount

        return income_result

    @staticmethod
    def get_outlay_result(article_list):
        """return outlay result"""
        outlay_result = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_OUTLAY:
                outlay_result += _article.amount

        return outlay_result

    @staticmethod
    def get_final_result(article_list):
        """return final result"""
        final_result = 0
        amount = 0

        for _article in article_list:
            if _article.article_type == ARTICLE_OUTLAY:
                amount = -(_article.amount)
            else:
                amount = _article.amount
            final_result += amount

        return final_result
