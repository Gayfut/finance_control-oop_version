from ui import basic_frame
from article import IncomeArticle


class IncomeFrame(basic_frame.BasicFrame):

    BTN_APPEND_TEXT = "Добавить доход"
    FRAME_TEXT = "Доход"

    def __init__(self, parent, articles_manager):
        super().__init__(parent, articles_manager)

    def _get_article(self, name, amount, category_name):
        article = IncomeArticle(name, amount, category_name)

        return article
