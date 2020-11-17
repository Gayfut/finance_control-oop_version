from tkinter import LabelFrame, Label, Listbox
from db import category_db


class ListFrame(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Список категорий", bg="orange", fg="black")

        self.__init_widgets()
        self.__place_widgets()
        self.show_categories()

    def __init_widgets(self):
        self.lbl_categories = Label(
            self, text="Названии категорий:", bg="orange", fg="black"
        )
        self.box_categories = Listbox(self, bg="black", fg="orange")

    def __place_widgets(self):
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
        self.__clean_box()

        categories_list = category_db.CategoryJSONManager.get_categories()

        for _category in categories_list:
            self.box_categories.insert("end", _category.name)

    def __clean_box(self):
        self.box_categories.delete(0, "end")
