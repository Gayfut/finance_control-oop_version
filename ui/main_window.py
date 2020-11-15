"""file for main window control"""
from tkinter import (
    Tk,
    LabelFrame,
    Button,
    Entry,
    Label,
    Listbox,
    OptionMenu,
    StringVar,
    Scrollbar,
    RIGHT,
    BOTH,
    messagebox,
)
from db import article_db
import settings
import article


class MainWindow:
    """control main_window"""

    def __init__(self):
        self.window = Tk()
        self.window.bind("<Destroy>", self.destroy)
        self.__configure_window()
        self.__init_frames()
        self.__place_frames()

    def mainloop(self):
        self.window.mainloop()

    def destroy(self, event):
        if event.widget == self.window:
            article_manager = article_db.ArticleBufferedJSONManager()
            article_manager.flush_articles()

    def __init_frames(self):
        self.income_frame = IncomeFrame(self.window)
        self.outlay_frame = OutlayFrame(self.window)

    def __place_frames(self):
        offset = 0.005
        frame_height = 0.4925
        frame_width = 0.4925
        outlay_frame_y = offset * 2 + frame_height

        self.income_frame.place(
            relx=offset, rely=offset, relwidth=frame_width, relheight=frame_height
        )
        self.outlay_frame.place(
            relx=offset,
            rely=outlay_frame_y,
            relwidth=frame_width,
            relheight=frame_height,
        )

    def __configure_window(self):
        """configure main_window"""
        self.window.title("FinanceControl")
        self.window.config(bg="grey")


class IncomeFrame(LabelFrame):
    """control income frame"""

    def __init__(self, parent):
        """create income frame"""
        super().__init__(parent, text="Доход", bg="orange", fg="black")

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        self.lbl_name = Label(self, text="Введите название:", bg="black", fg="orange")
        self.ent_name = Entry(self, bg="black", fg="orange")
        self.lbl_sum = Label(self, text="Введите сумму:", bg="black", fg="orange")
        self.ent_sum = Entry(self, bg="black", fg="orange")
        self.btn_income = Button(
            self,
            name="income",
            text="Добавить доход",
            bg="black",
            fg="orange",
            command=self.__btn_income_handler,
        )

        self.lbl_category = Label(
            self, text="Выберите категорию:", bg="black", fg="orange"
        )

        self.categories = settings.DEFAULT_CATEGORIES_LIST
        self.selection_category = StringVar(self)
        self.selection_category.set(self.categories[0])
        self.menu_categories = OptionMenu(
            self, self.selection_category, *self.categories
        )
        self.menu_categories.config(bg="black", fg="orange")

        self.btn_categories = Button(self, text="+", bg="black", fg="orange")

    def __place_widgets(self):
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
        btn_income_width = 0.5
        btn_income_height = 0.2
        btn_income_y = ent_name_y * 6 + offset * 6
        btn_income_x = (1 - offset * 2 - btn_income_width) / 2

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
        self.btn_income.place(
            relx=btn_income_x,
            rely=btn_income_y,
            relwidth=btn_income_width,
            relheight=btn_income_height,
        )

    def __btn_income_handler(self):
        name = self.ent_name.get()
        try:
            amount = int(self.ent_sum.get())
        except ValueError:
            messagebox.showwarning("Предупреждение!", "Пожалуйста, введите число!")
            return
        category_name = self.selection_category.get()

        income_article = article.IncomeArticle(name, amount, category_name)
        articles_manager = article_db.ArticleBufferedJSONManager()
        articles_manager.save_article(income_article)

        self.__clean_entry()

    def __clean_entry(self):
        """clean entry margins"""
        self.ent_name.delete(0, "end")
        self.ent_sum.delete(0, "end")


class OutlayFrame(LabelFrame):
    """control outlay frame"""

    def __init__(self, parent):
        """create outlay frame"""
        super().__init__(parent, text="Расход", bg="orange", fg="black")

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        self.lbl_name = Label(self, text="Введите название:", bg="black", fg="orange")
        self.ent_name = Entry(self, bg="black", fg="orange")
        self.lbl_sum = Label(self, text="Введите сумму:", bg="black", fg="orange")
        self.ent_sum = Entry(self, bg="black", fg="orange")
        self.btn_outlay = Button(
            self,
            name="income",
            text="Добавить расход",
            bg="black",
            fg="orange",
            command=self.__btn_outlay_handler,
        )

        self.lbl_category = Label(
            self, text="Выберите категорию:", bg="black", fg="orange"
        )

        self.categories = settings.DEFAULT_CATEGORIES_LIST
        self.selection_category = StringVar(self)
        self.selection_category.set(self.categories[0])
        self.menu_categories = OptionMenu(
            self, self.selection_category, *self.categories
        )
        self.menu_categories.config(bg="black", fg="orange")

        self.btn_categories = Button(self, text="+", bg="black", fg="orange")

    def __place_widgets(self):
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
        btn_outlay_width = 0.5
        btn_outlay_height = 0.2
        btn_outlay_y = ent_name_y * 6 + offset * 6
        btn_outlay_x = (1 - offset * 2 - btn_outlay_width) / 2

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
        self.btn_outlay.place(
            relx=btn_outlay_x,
            rely=btn_outlay_y,
            relwidth=btn_outlay_width,
            relheight=btn_outlay_height,
        )

    def __btn_outlay_handler(self):
        name = self.ent_name.get()
        try:
            amount = int(self.ent_sum.get())
        except ValueError:
            messagebox.showwarning("Предупреждение!", "Пожалуйста, введите число!")
            return
        category_name = self.selection_category.get()

        outlay_article = article.OutlayArticle(name, amount, category_name)
        articles_manager = article_db.ArticleBufferedJSONManager()
        articles_manager.save_article(outlay_article)

        self.__clean_entry()

    def __clean_entry(self):
        """clean entry margins"""
        self.ent_name.delete(0, "end")
        self.ent_sum.delete(0, "end")
