"""file control specification of list frame on category window"""
from tkinter import LabelFrame, Label, Listbox
from db.category_db import CategoryJSONManager


class ListFrame(LabelFrame):
    """control list frame"""

    def __init__(self, parent):
        """create list frame"""
        super().__init__(parent, text="Список категорий", bg="orange", fg="black")

        self.__init_widgets()
        self.__place_widgets()
        self.show_categories()

    def __init_widgets(self):
        """create list widgets"""
        self.lbl_categories = Label(
            self, text="Названии категорий:", bg="orange", fg="black"
        )
        self.box_categories = Listbox(self, bg="black", fg="orange")

    def __place_widgets(self):
        """pack list widgets"""
        offset = 0.01
        widget_width = 0.98
        lbl_height = 0.05
        box_categories_y = offset * 2 + lbl_height
        box_categories_height = 1 - offset * 2 - lbl_height

        self.lbl_categories.place(
            relx=offset, rely=offset, relwidth=widget_width, relheight=lbl_height
        )
        self.box_categories.place(
            relx=offset,
            rely=box_categories_y,
            relwidth=widget_width,
            relheight=box_categories_height,
        )

    def show_categories(self):
        """show categories in list box"""
        self.__clean_box()

        categories_list = CategoryJSONManager.get_categories()

        for _category in categories_list:
            self.box_categories.insert("end", _category.name)

    def __clean_box(self):
        """clean list box"""
        self.box_categories.delete(0, "end")
