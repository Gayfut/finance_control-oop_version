"""file for control specification of income frame"""
from ui.basic_frame import BasicFrame
from income_article import IncomeArticle


class IncomeFrame(BasicFrame):
    """control income frame"""

    BTN_APPEND_TEXT = "Добавить доход"
    FRAME_TEXT = "Доход"

    def __init__(self, parent, articles_manager, result_frame):
        """create income frame"""
        super().__init__(parent, articles_manager, result_frame)

    def _get_article(self, name, amount, category_name):
        """create and return income article"""
        article = IncomeArticle(name, amount, category_name)

        return article
