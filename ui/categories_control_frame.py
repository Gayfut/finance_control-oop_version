from tkinter import LabelFrame, Entry, Button
from category import Category
from db import category_db


class ControlFrame(LabelFrame):
    def __init__(self, parent, list_frame):
        super().__init__(parent, text="Управление", bg="orange", fg="black")

        self.list_frame = list_frame

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        self.ent_new_category = Entry(self, bg="black", fg="orange")
        self.btn_new_category = Button(
            self,
            text="Добавить",
            bg="black",
            fg="orange",
            command=self.__btn_new_category_handler,
        )
        self.btn_delete_category = Button(
            self,
            text="Удалить",
            bg="black",
            fg="orange",
            command=self.__btn_delete_category_handler,
        )

    def __place_widgets(self):
        offset = 0.01
        ent_new_category_width = 0.7
        widget_height = 0.1
        btn_new_category_x = offset * 2 + ent_new_category_width
        btn_new_category_width = 1 - ent_new_category_width - offset * 3
        btn_delete_category_width = btn_new_category_x
        btn_delete_category_y = widget_height + offset * 2

        self.ent_new_category.place(
            relx=offset,
            rely=offset,
            relwidth=ent_new_category_width,
            relheight=widget_height,
        )
        self.btn_new_category.place(
            relx=btn_new_category_x,
            rely=offset,
            relwidth=btn_new_category_width,
            relheight=widget_height,
        )
        self.btn_delete_category.place(
            relx=offset,
            rely=btn_delete_category_y,
            relwidth=btn_delete_category_width,
            relheight=widget_height,
        )

    def __btn_new_category_handler(self):
        new_category_name = self.ent_new_category.get()

        new_category = Category(new_category_name)

        category_db.CategoryJSONManager.save_category(new_category)

        self.list_frame.show_categories()

    def __btn_delete_category_handler(self):
        selection_category = self.list_frame.box_categories.curselection()
        selection_category = selection_category[0]
        if not selection_category:
            return None

        category_db.CategoryJSONManager.delete_category(selection_category)
        self.list_frame.box_categories.delete(selection_category)
