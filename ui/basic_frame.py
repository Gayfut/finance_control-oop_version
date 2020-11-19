from tkinter import LabelFrame, Label, Entry, Button, StringVar, OptionMenu, messagebox
from ui import categories_window
from db import category_db


class BasicFrame(LabelFrame):
    """control income frame"""

    BTN_APPEND_TEXT = None
    FRAME_TEXT = None

    def __init__(self, parent, articles_manager, result_frame):
        """create income frame"""
        super().__init__(parent, text=self.FRAME_TEXT, bg="orange", fg="black")

        self.__articles_manager = articles_manager
        self.result_frame = result_frame

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        """create income widgets"""
        # values entry widgets
        self.lbl_name = Label(self, text="Введите название:", bg="black", fg="orange")
        self.ent_name = Entry(self, bg="black", fg="orange")
        self.lbl_sum = Label(self, text="Введите сумму:", bg="black", fg="orange")
        self.ent_sum = Entry(self, bg="black", fg="orange")
        self.btn_append_article = Button(
            self,
            text=self.BTN_APPEND_TEXT,
            bg="black",
            fg="orange",
            command=self.__btn_article_handler,
        )

        # category widgets
        self.lbl_category = Label(
            self, text="Выберите категорию:", bg="black", fg="orange"
        )

        categories = category_db.CategoryJSONManager.get_categories()
        categories_names = []
        for _category in categories:
            _category_name = _category.name
            categories_names.append(_category_name)

        self.selection_category = StringVar(self)
        self.selection_category.set(categories_names[0])
        self.menu_categories = OptionMenu(
            self, self.selection_category, *categories_names
        )
        self.menu_categories.config(bg="black", fg="orange")
        self.btn_categories = Button(
            self,
            text="+",
            bg="black",
            fg="orange",
            command=self.__btn_categories_handler,
        )

    def __place_widgets(self):
        """pack income widgets"""
        offset = 0.01
        widget_width = 0.99
        widget_height = 0.1
        ent_name_y = offset + widget_height
        lbl_sum_y = ent_name_y * 2 + offset
        ent_sum_y = lbl_sum_y + widget_height
        lbl_category_y = ent_name_y * 4 + offset
        menu_categories_y = lbl_category_y + widget_height
        menu_categories_width = 0.7
        btn_categories_x = menu_categories_width + offset * 2
        btn_categories_width = 1 - btn_categories_x - offset
        btn_article_width = 0.5
        btn_article_height = 0.2
        btn_article_y = ent_name_y * 6 + offset * 6
        btn_article_x = (1 - offset * 2 - btn_article_width) / 2

        self.lbl_name.place(
            relx=offset, rely=offset, relwidth=widget_width, relheight=widget_height
        )
        self.ent_name.place(
            relx=offset, rely=ent_name_y, relwidth=widget_width, relheight=widget_height
        )
        self.lbl_sum.place(
            relx=offset, rely=lbl_sum_y, relwidth=widget_width, relheight=widget_height
        )
        self.ent_sum.place(
            relx=offset, rely=ent_sum_y, relwidth=widget_width, relheight=widget_height
        )
        self.lbl_category.place(
            relx=offset,
            rely=lbl_category_y,
            relwidth=widget_width,
            relheight=widget_height,
        )
        self.menu_categories.place(
            relx=offset,
            rely=menu_categories_y,
            relwidth=menu_categories_width,
            relheight=widget_height,
        )
        self.btn_categories.place(
            relx=btn_categories_x,
            rely=menu_categories_y,
            relwidth=btn_categories_width,
            relheight=widget_height,
        )
        self.btn_append_article.place(
            relx=btn_article_x,
            rely=btn_article_y,
            relwidth=btn_article_width,
            relheight=btn_article_height,
        )

    def _get_article(self, name, amount, category_name):
        raise NotImplementedError()

    def __btn_article_handler(self):
        """get values from entry margins, create income article and save it"""
        name = self.ent_name.get()
        try:
            amount = int(self.ent_sum.get())
        except ValueError:
            messagebox.showwarning("Предупреждение!", "Пожалуйста, введите число!")
            return
        category_name = self.selection_category.get()

        new_article = self._get_article(name, amount, category_name)

        self.__articles_manager.save_article(new_article)

        self.__clean_entry()
        self.result_frame.show_articles_unsorted()

    def __btn_categories_handler(self):
        self.category_window = categories_window.CategoryWindow(
            self.menu_categories, self.selection_category
        )

    def __clean_entry(self):
        """clean entry margins"""
        self.ent_name.delete(0, "end")
        self.ent_sum.delete(0, "end")
