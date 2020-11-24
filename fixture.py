"""file for create and control fixture"""
from datetime import datetime, date
from random import choice, randint
from income_article import IncomeArticle
from outlay_article import OutlayArticle
import settings


class FixtureManager:
    """control fixture"""

    NAMES = [
        "Хлеб",
        "Молоко",
        "Бензин",
        "Вода",
        "Куртка",
        "Часы",
        "Премия",
        "Диван",
    ]

    def __init__(self, articles_manager):
        self.__articles_manager = articles_manager

        self.__save_fixture()

    def __get_name(self):
        """create and return random name"""
        name = choice(self.NAMES)

        return name

    def __get_amount(self, name):
        """create and return random amount"""
        amount_map = {
            self.NAMES[0]: (-50, -30),
            self.NAMES[1]: (-100, -60),
            self.NAMES[2]: (-3000, -1000),
            self.NAMES[3]: (-1000, -200),
            self.NAMES[4]: (-10000, -5000),
            self.NAMES[5]: (-10000, 10000),
            self.NAMES[6]: (5000, 30000),
            self.NAMES[7]: (-30000, -10000),
        }

        try:
            amount = amount_map[name]
        except KeyError:
            amount = None
        amount_min, amount_max = amount[0], amount[1]
        amount = randint(amount_min, amount_max)

        return amount

    def __get_article_type(self, amount):
        """create and return random article type"""
        if amount <= 0:
            type_name = settings.ARTICLE_OUTLAY
        else:
            type_name = settings.ARTICLE_INCOME

        return type_name

    def __get_date(self):
        """create and return random date"""
        year = randint(2018, datetime.today().year)
        month = randint(1, 12)

        mouths_with_31 = [1, 3, 5, 7, 8, 10, 12]
        if month in mouths_with_31:
            day = randint(1, 31)
        elif month == 2:
            day = randint(1, 28)
        else:
            day = randint(1, 30)

        date_create = date(year, month, day)

        return date_create

    def __get_category(self, name):
        """create and return random category"""
        category_map = {
            self.NAMES[0]: settings.DEFAULT_CATEGORIES_LIST[0],
            self.NAMES[1]: settings.DEFAULT_CATEGORIES_LIST[0],
            self.NAMES[2]: settings.DEFAULT_CATEGORIES_LIST[1],
            self.NAMES[3]: settings.DEFAULT_CATEGORIES_LIST[2],
            self.NAMES[4]: settings.DEFAULT_CATEGORIES_LIST[3],
            self.NAMES[5]: settings.DEFAULT_CATEGORIES_LIST[4],
            self.NAMES[6]: settings.DEFAULT_CATEGORIES_LIST[5],
            self.NAMES[7]: settings.DEFAULT_CATEGORIES_LIST[6],
        }

        try:
            category = category_map[name]
        except KeyError:
            category = None

        return category

    def __get_article(self):
        """get attributes, create and return article"""
        name = self.__get_name()
        amount = self.__get_amount(name)
        article_type = self.__get_article_type(amount)
        date_create = self.__get_date()
        category = self.__get_category(name)

        if article_type == settings.ARTICLE_INCOME:
            article = IncomeArticle(name, amount, category, date_create=date_create)
        else:
            article = OutlayArticle(name, amount, category, date_create=date_create)

        return article

    def get_fixture_articles(self):
        """create and return fixture article list"""
        fixture_article_list = []

        for _step in range(51):
            _article = self.__get_article()
            fixture_article_list.append(_article)

        return fixture_article_list

    def __save_fixture(self):
        """save fixture article list in DB"""
        fixture_article_list = self.get_fixture_articles()

        self.__articles_manager.save_articles(fixture_article_list)
