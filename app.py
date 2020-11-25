"""file for control app specifications"""
from ui.main_window import MainWindow
from db.article_db import ArticleBufferedJSONManager


class Application:
    """control app"""

    def __init__(self):
        """create main_window"""
        self.__articles_manager = ArticleBufferedJSONManager()
        self.main_window = MainWindow(articles_manager=self.__articles_manager)

    def start(self):
        """start app"""
        self.main_window.mainloop()

    def stop(self):
        """stop app"""
        self.main_window.destroy()
