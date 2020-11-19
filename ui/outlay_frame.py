from ui import basic_frame
from article import OutlayArticle


class OutlayFrame(basic_frame.BasicFrame):

    BTN_APPEND_TEXT = "Добавить расход"
    FRAME_TEXT = "Расход"

    def __init__(self, parent, articles_manager, result_frame):
        super().__init__(parent, articles_manager, result_frame)

    def _get_article(self, name, amount, category_name):
        article = OutlayArticle(name, amount, category_name)

        return article
