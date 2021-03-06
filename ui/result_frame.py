"""file for control specification of result frame"""
from tkinter import (
    LabelFrame,
    Listbox,
    Scrollbar,
    RIGHT,
    BOTH,
    Label,
    Button,
    StringVar,
    OptionMenu,
    Entry,
    messagebox,
)
from datetime import datetime
from re import search
from settings import (
    CATEGORY_ALL,
    ARTICLE_INCOME_NAME,
    ARTICLE_OUTLAY_NAME,
    ARTICLE_INCOME,
    ARTICLE_OUTLAY,
    DATE_FORMAT,
)
from db.category_db import CategoryJSONManager
from db.result_db import ResultManager
from fixture import FixtureManager
from sort import Sorter


class ResultFrame(LabelFrame):
    """control result frame"""

    def __init__(self, parent, articles_manager):
        """create result frame"""
        super().__init__(parent, text="Результаты", bg="orange", fg="black")

        self.__articles_manager = articles_manager

        self.__init_widgets()
        self.__place_widgets()
        self.show_articles_unsorted()
        self.show_result_unsorted()

    def __init_widgets(self):
        """create result widgets"""
        # result widgets
        self.box_result = Listbox(self, bg="black", fg="orange")
        self.sb_result = Scrollbar(self.box_result, bg="black")

        self.sb_result.pack(side=RIGHT, fill=BOTH)
        self.box_result.config(yscrollcommand=self.sb_result.set)
        self.sb_result.config(command=self.box_result.yview)

        self.lbl_incomes = Label(self, bg="black", fg="green")
        self.lbl_outlays = Label(self, bg="black", fg="red")
        self.lbl_result = Label(self, bg="black", fg="orange")

        self.btn_del = Button(
            self,
            text="Удалить",
            bg="black",
            fg="orange",
            command=self.__btn_delete_handler,
        )
        self.btn_clean_box = Button(
            self,
            text="Очистить",
            bg="black",
            fg="orange",
            command=self.__btn_clean_handler,
        )

        # demo widget
        self.btn_demo = Button(
            self,
            text="Демо",
            bg="black",
            fg="orange",
            command=self.__btn_demo_handler,
        )

        # sort widgets
        sort_types = [
            CATEGORY_ALL,
            ARTICLE_INCOME_NAME,
            ARTICLE_OUTLAY_NAME,
        ]
        self.sort_selection_type = StringVar(self)
        self.sort_selection_type.set(sort_types[0])
        self.menu_sort_types = OptionMenu(self, self.sort_selection_type, *sort_types)
        self.menu_sort_types.config(bg="black", fg="orange")
        self.menu_sort_types_in_menu = self.menu_sort_types.children["menu"]
        self.menu_sort_types_in_menu.bind("<Leave>", self.__sort_handler)

        sort_categories = CategoryJSONManager.get_categories()
        sort_categories_names = []
        for _category in sort_categories:
            _category_name = _category.name
            sort_categories_names.append(_category_name)

        sort_categories_names.insert(0, CATEGORY_ALL)
        self.sort_selection_category = StringVar(self)
        self.sort_selection_category.set(sort_categories_names[0])
        self.menu_sort_categories = OptionMenu(
            self, self.sort_selection_category, *sort_categories_names
        )
        self.menu_sort_categories.config(bg="black", fg="orange")
        self.menu_sort_categories_in_menu = self.menu_sort_categories["menu"]
        self.menu_sort_categories_in_menu.bind("<Leave>", self.__sort_handler)

        self.ent_sort_date_start = Entry(self, bg="black", fg="orange")
        self.ent_sort_date_end = Entry(self, bg="black", fg="orange")
        self.btn_sort_by_date = Button(
            self, text="Отсортировать", bg="black", fg="orange"
        )
        self.btn_sort_by_date.bind("<Button-1>", self.__sort_handler)

    def __place_widgets(self):
        """pack result widgets"""
        offset = 0.01
        sort_widget_width = 0.2
        sort_widget_height = 0.05
        menu_sort_categories_x = offset * 2 + sort_widget_width
        ent_sort_date_start_x = menu_sort_categories_x + offset + sort_widget_width
        ent_sort_date_end_x = ent_sort_date_start_x + sort_widget_width
        btn_sort_by_date_x = ent_sort_date_end_x + offset + sort_widget_width
        btn_sort_by_date_width = 0.15
        box_result_width = 0.98
        result_widget_width = 0.32
        result_btn_height = 0.1
        box_result_height = 0.6
        result_lbl_height = 0.06
        box_result_y = sort_widget_height + offset * 2
        lbl_results_y = box_result_y + box_result_height
        btn_results_y = lbl_results_y + result_lbl_height
        lbl_outlays_x = offset * 2 + result_widget_width
        lbl_result_x = lbl_outlays_x + offset + result_widget_width

        self.menu_sort_types.place(
            relx=offset,
            rely=offset,
            relwidth=sort_widget_width,
            relheight=sort_widget_height,
        )
        self.menu_sort_categories.place(
            relx=menu_sort_categories_x,
            rely=offset,
            relwidth=sort_widget_width,
            relheight=sort_widget_height,
        )
        self.ent_sort_date_start.place(
            relx=ent_sort_date_start_x,
            rely=offset,
            relwidth=sort_widget_width,
            relheight=sort_widget_height,
        )
        self.ent_sort_date_end.place(
            relx=ent_sort_date_end_x,
            rely=offset,
            relwidth=sort_widget_width,
            relheight=sort_widget_height,
        )
        self.btn_sort_by_date.place(
            relx=btn_sort_by_date_x,
            rely=offset,
            relwidth=btn_sort_by_date_width,
            relheight=sort_widget_height,
        )
        self.box_result.place(
            relx=offset,
            rely=box_result_y,
            relwidth=box_result_width,
            relheight=box_result_height,
        )
        self.lbl_incomes.place(
            relx=offset,
            rely=lbl_results_y,
            relwidth=result_widget_width,
            relheight=result_lbl_height,
        )
        self.lbl_outlays.place(
            relx=lbl_outlays_x,
            rely=lbl_results_y,
            relwidth=result_widget_width,
            relheight=result_lbl_height,
        )
        self.lbl_result.place(
            relx=lbl_result_x,
            rely=lbl_results_y,
            relwidth=result_widget_width,
            relheight=result_lbl_height,
        )
        self.btn_del.place(
            relx=offset,
            rely=btn_results_y,
            relwidth=result_widget_width,
            relheight=result_btn_height,
        )
        self.btn_clean_box.place(
            relx=lbl_outlays_x,
            rely=btn_results_y,
            relwidth=result_widget_width,
            relheight=result_btn_height,
        )
        self.btn_demo.place(
            relx=lbl_result_x,
            rely=btn_results_y,
            relwidth=result_widget_width,
            relheight=result_btn_height,
        )

    def show_articles_unsorted(self):
        """show unsorted articles in list box"""
        article_list = self.__articles_manager.get_articles()
        self.show_articles(article_list)

    def show_articles(self, article_list):
        """show certain articles in list box"""
        self.__clean_box()

        for _article in article_list:
            name = _article.name
            amount = _article.amount
            article_type = _article.article_type
            date_create = _article.date_create
            category_name = _article.category
            article_id = _article.article_id

            name = name.rjust(10, " ")
            amount = str(amount).rjust(6, " ")

            if article_type == ARTICLE_INCOME:
                self.box_result.insert(
                    0,
                    f"{article_type} {name} {amount} {category_name} {date_create} {article_id}",
                )
                self.box_result.itemconfig(0, {"bg": "green"})
            elif article_type == ARTICLE_OUTLAY:
                self.box_result.insert(
                    0,
                    f"{article_type} {name} {amount} {category_name} {date_create} {article_id}",
                )
                self.box_result.itemconfig(0, {"bg": "red"})

    def show_result_unsorted(self):
        """show unsorted results in labels"""
        article_list = self.__articles_manager.get_articles()
        self.show_result(article_list)

    def show_result(self, article_list):
        """show certain results in labels"""
        income_result = ResultManager.get_income_result(article_list)
        self.lbl_incomes["text"] = f"Доходы: {income_result}"

        outlay_result = ResultManager.get_outlay_result(article_list)
        self.lbl_outlays["text"] = f"Расходы: {outlay_result}"

        final_result = ResultManager.get_final_result(article_list)
        self.lbl_result["text"] = f"Итог: {final_result}"
        if final_result > 0:
            self.lbl_result["fg"] = "green"
        elif final_result < 0:
            self.lbl_result["fg"] = "red"
        else:
            self.lbl_result["fg"] = "orange"

    def __btn_delete_handler(self):
        """get selection article from list box, create article and delete it from article db"""
        selection_article_index = self.box_result.curselection()
        selection_article_index = selection_article_index[0]
        selection_article = self.box_result.get(selection_article_index)
        selection_article_id = search("id\d+", selection_article).group(0)

        if not selection_article_id:
            return None

        self.__articles_manager.delete_article(selection_article_id)
        self.box_result.delete(selection_article_index)
        self.show_result_unsorted()

    def __btn_clean_handler(self):
        """clean article buffer, article list and list box"""
        clear_article_list = []

        self.__articles_manager.clean_all()
        self.show_result(clear_article_list)
        self.__clean_box()

    def __btn_demo_handler(self):
        """create fixture, save and show it"""
        fixture = FixtureManager(self.__articles_manager)
        fixture_article_list = fixture.get_fixture_articles()

        self.show_articles(fixture_article_list)
        self.show_result(fixture_article_list)

    def __sort_handler(self, event):
        """get values from sort margins, validate it and sort by params"""
        sort_date_start = self.ent_sort_date_start.get()
        sort_date_end = self.ent_sort_date_end.get()
        sort_type = self.sort_selection_type.get()
        sort_category = self.sort_selection_category.get()

        if sort_date_start and sort_date_end:
            try:
                sort_start = datetime.strptime(sort_date_start, DATE_FORMAT).date()
                sort_end = datetime.strptime(sort_date_end, DATE_FORMAT).date()
            except ValueError:
                messagebox.showwarning(
                    "Предупреждение!",
                    "Введите даты в формате 1970-01-01 (год-месяц-день).",
                )
            self.__clean_entry()
        elif sort_date_start:
            try:
                sort_start = datetime.strptime(sort_date_start, DATE_FORMAT).date()
                sort_end = datetime.today().date()
            except ValueError:
                messagebox.showwarning(
                    "Предупреждение!",
                    "Введите даты в формате 1970-01-01 (год-месяц-день).",
                )
            self.__clean_entry()
        elif sort_date_end:
            messagebox.showwarning("Предупреждение!", "Введите начало периода.")
            self.__clean_entry()
        else:
            sort_start = None
            sort_end = None

        if sort_type == ARTICLE_INCOME_NAME:
            sort_type = ARTICLE_INCOME
        elif sort_type == ARTICLE_OUTLAY_NAME:
            sort_type = ARTICLE_OUTLAY
        else:
            sort_type = None

        if sort_category == CATEGORY_ALL:
            sort_category = None

        sorter = Sorter(self.__articles_manager)
        try:
            sorted_article_list = sorter.sort_articles(
                sort_type, sort_category, sort_start, sort_end
            )
        except UnboundLocalError:
            sorted_article_list = sorter.sort_articles(sort_type, sort_category)

        self.show_articles(sorted_article_list)
        self.show_result(sorted_article_list)

    def __clean_box(self):
        """clean list box"""
        self.box_result.delete(0, "end")

    def __clean_entry(self):
        """clean entry margins"""
        self.ent_sort_date_start.delete(0, "end")
        self.ent_sort_date_end.delete(0, "end")
