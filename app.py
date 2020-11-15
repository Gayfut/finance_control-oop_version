"""file for control app specifications"""
from ui import main_window


class Application:
    """control app"""

    def __init__(self):
        """create main_window"""
        self.main_window = main_window.MainWindow()

    def start(self):
        """start app"""
        self.main_window.mainloop()

    def stop(self):
        """stop app"""
        self.main_window.destroy()
