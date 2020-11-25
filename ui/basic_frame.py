"""file control specification of base frame for articles"""
from tkinter import LabelFrame, Label, Entry, Button, StringVar, OptionMenu, messagebox
from ui.categories_window import CategoryWindow
from db.category_db import CategoryJSONManager


class BasicFrame(LabelFrame):
    """control article frame"""

    BTN_APPEND_TEXT = None
    FRAME_TEXT = None

    def __init__(self, parent, articles_manager, result_frame):
        """create article frame"""
        super().__init__(parent, text=self.FRAME_TEXT, bg="orange", fg="black")

        self.__articles_manager = articles_manager
        self.result_frame = result_frame

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        """create article widgets"""
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

        categories = CategoryJSONManager.get_categories()
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
        """pack article widgets"""
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
        """create and return article"""
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

        check_status = self.__check_article_on_repeat(new_article)
        if check_status is True:
            self.__articles_manager.save_article(new_article)
        else:
            self.__clean_entry()
            return

        self.__clean_entry()
        self.result_frame.show_articles_unsorted()
        self.result_frame.show_result_unsorted()

    def __btn_categories_handler(self):
        """create category window"""
        self.category_window = CategoryWindow(self.__refresh_categories)

    def __refresh_categories(self):
        """refresh categories in option menu on main window"""
        categories = CategoryJSONManager.get_categories()
        categories_names = []
        for _category in categories:
            _category_name = _category.name
            categories_names.append(_category_name)

        self.menu_categories.children["menu"].delete(0, "end")
        self.result_frame.menu_sort_categories.children["menu"].delete(0, "end")

        for _category in categories_names:
            self.menu_categories.children["menu"].add_command(
                label=_category,
                command=lambda veh=_category: self.selection_category.set(veh),
            )
            self.result_frame.menu_sort_categories.children["menu"].add_command(
                label=_category,
                command=lambda veh=_category: self.result_frame.sort_selection_category.set(
                    veh
                ),
            )

    def __check_article_on_repeat(self, new_article):
        """check new article on repeat in article DB"""
        article_buffer = self.__articles_manager.get_article_buffer()
        article_list = self.__articles_manager.get_articles()
        article_buffer.extend(article_list)

        for _article in article_buffer:
            if (
                (new_article.name == _article.name)
                and (new_article.amount == _article.amount)
                and (new_article.article_type == _article.article_type)
                and (new_article.category == _article.category)
            ):
                messagebox.showwarning(
                    "Предупреждение!", "Такой артикл уже существует!"
                )
                return False
        return True

    def __clean_entry(self):
        """clean entry margins"""
        self.ent_name.delete(0, "end")
        self.ent_sum.delete(0, "end")
