"""file for control app specifications"""
from ui import main_window
from db import article_db


class Application:
    """control app"""

    def __init__(self):
        """create main_window"""
        self.__articles_manager = article_db.ArticleBufferedJSONManager()
        self.main_window = main_window.MainWindow(
            articles_manager=self.__articles_manager
        )

    def start(self):
        """start app"""
        self.main_window.mainloop()

    def stop(self):
        """stop app"""
        self.main_window.destroy()
