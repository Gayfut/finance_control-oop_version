"""file for control specification of outlay frame"""
from ui import basic_frame
from outlay_article import OutlayArticle


class OutlayFrame(basic_frame.BasicFrame):
    """control outlay frame"""

    BTN_APPEND_TEXT = "Добавить расход"
    FRAME_TEXT = "Расход"

    def __init__(self, parent, articles_manager, result_frame):
        """create outlay frame"""
        super().__init__(parent, articles_manager, result_frame)

    def _get_article(self, name, amount, category_name):
        """create and return outlay article"""
        article = OutlayArticle(name, amount, category_name)

        return article
