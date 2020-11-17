from tkinter import Toplevel
from db import category_db
from ui import categories_control_frame, categories_list_frame


class CategoryWindow:
    def __init__(self, main_frames_menu_categories, main_frames_selection_category):
        self.window = Toplevel()

        self.main_frames_menu_categories = main_frames_menu_categories
        self.main_frames_selection_category = main_frames_selection_category

        self.__configure_window()
        self.__init_frames()
        self.__place_frames()

    def __configure_window(self):
        self.window.config(bg="black")
        self.window.title("Категории")
        self.window.geometry("640x480")
        self.window.grab_set()

        self.window.bind("<Destroy>", self.__refresh_categories)

    def __init_frames(self):
        self.list_frame = categories_list_frame.ListFrame(self.window)
        self.control_frame = categories_control_frame.ControlFrame(
            self.window, self.list_frame
        )

    def __place_frames(self):
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

    def __refresh_categories(self, event):
        """обновляет спиок категорий в option menu на главной странице"""
        categories = category_db.CategoryJSONManager.get_categories()
        categories_names = []
        for _category in categories:
            _category_name = _category.name
            categories_names.append(_category_name)

        self.main_frames_menu_categories.children["menu"].delete(0, "end")
        # self.menu_sort_categories.children["menu"].delete(0, "end")

        for _category in categories_names:
            self.main_frames_menu_categories.children["menu"].add_command(
                label=_category,
                command=lambda veh=_category: self.main_frames_selection_category.set(
                    veh
                ),
            )
            # self.menu_sort_categories.children["menu"].add_command(
            #     label=_category,
            #     command=lambda veh=_category: self.sort_selection_category.set(veh),
            # )
