"""file for main window control"""
from tkinter import (
    Tk,
)
from ui import income_frame, outlay_frame, result_frame


class MainWindow:
    """control main_window"""

    def __init__(self, articles_manager):
        self.window = Tk()
        self.window.bind("<Destroy>", self.destroy)

        self.__articles_manager = articles_manager

        self.__configure_window()
        self.__init_frames()
        self.__place_frames()

    def mainloop(self):
        """start mainloop"""
        self.window.mainloop()

    def destroy(self, event):
        """destroy window"""
        if event.widget == self.window:
            self.__articles_manager.flush_articles()

    def __init_frames(self):
        """create frames"""
        self.result_frame = result_frame.ResultFrame(
            self.window, self.__articles_manager
        )
        self.income_frame = income_frame.IncomeFrame(
            self.window, self.__articles_manager, self.result_frame
        )
        self.outlay_frame = outlay_frame.OutlayFrame(
            self.window, self.__articles_manager, self.result_frame
        )

    def __place_frames(self):
        """pack frames"""
        offset = 0.005
        frame_height = 0.4925
        frame_width = 0.4925
        outlay_frame_y = offset * 2 + frame_height
        result_frame_x = frame_width + offset * 2
        result_frame_height = frame_height + outlay_frame_y - offset

        self.income_frame.place(
            relx=offset, rely=offset, relwidth=frame_width, relheight=frame_height
        )
        self.outlay_frame.place(
            relx=offset,
            rely=outlay_frame_y,
            relwidth=frame_width,
            relheight=frame_height,
        )
        self.result_frame.place(
            relx=result_frame_x,
            rely=offset,
            relwidth=frame_width,
            relheight=result_frame_height,
        )

    def __configure_window(self):
        """configure main_window"""
        self.window.title("FinanceControl")
        self.window.config(bg="black")
        width_window = self.window.winfo_screenwidth()
        height_window = self.window.winfo_screenheight()
        self.window.geometry(f"{width_window}x{height_window}")
