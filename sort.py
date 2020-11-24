"""file for sorting control"""
import settings


class Sorter:
    """control sorting"""

    def __init__(self, articles_manager):
        self.__articles_manager = articles_manager

    def sort_articles(
        self,
        sort_type_name,
        sort_category_name,
        sort_date_start=None,
        sort_date_end=None,
    ):
        """get params and sort by him"""
        articles_list = self.__articles_manager.get_articles()
        sorted_article_list = []

        for _article in articles_list:
            if (
                sort_type_name in (settings.ARTICLE_INCOME, settings.ARTICLE_OUTLAY)
                and _article.article_type != sort_type_name
            ):
                continue
            if sort_category_name and _article.category != sort_category_name:
                continue
            if sort_date_start and _article.date_create < sort_date_start:
                continue
            if sort_date_end and _article.date_create > sort_date_end:
                continue

            sorted_article_list.append(_article)

        return sorted_article_list
