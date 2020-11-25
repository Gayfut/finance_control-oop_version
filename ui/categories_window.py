"""file for control specification of category window"""
from tkinter import Toplevel
from ui.categories_control_frame import ControlFrame
from ui.categories_list_frame import ListFrame


class CategoryWindow:
    """control category window"""

    def __init__(self, on_destroy_callback):
        """create category window"""
        self.window = Toplevel()

        self.on_destroy_callback = on_destroy_callback

        self.__configure_window()
        self.__init_frames()
        self.__place_frames()

    def __configure_window(self):
        """configure category window"""
        self.window.config(bg="black")
        self.window.title("Категории")
        self.window.geometry("640x480")
        self.window.grab_set()

        self.window.bind("<Destroy>", self.__on_destroy)

    def __init_frames(self):
        """create frames for category window"""
        self.list_frame = ListFrame(self.window)
        self.control_frame = ControlFrame(self.window, self.list_frame)

    def __place_frames(self):
        """pack frames on category window"""
        offset = 0.005
        frame_height = 0.99
        frame_width = 0.4925
        control_frame_x = offset * 2 + frame_width

        self.list_frame.place(
            relx=offset, rely=offset, relwidth=frame_width, relheight=frame_height
        )
        self.control_frame.place(
            relx=control_frame_x,
            rely=offset,
            relwidth=frame_width,
            relheight=frame_height,
        )

    def __on_destroy(self, event):
        self.on_destroy_callback()
