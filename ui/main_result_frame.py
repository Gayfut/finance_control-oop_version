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
)
from settings import CATEGORY_ALL, ARTICLE_INCOME_NAME, ARTICLE_OUTLAY_NAME
from db import category_db


class ResultFrame(LabelFrame):
    def __init__(self, parent, articles_manager):
        """create income frame"""
        super().__init__(parent, text="Результаты", bg="orange", fg="black")

        self.__articles_manager = articles_manager

        self.__init_widgets()
        self.__place_widgets()

    def __init_widgets(self):
        # виджеты результатов
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
        )
        self.btn_clean_box = Button(
            self,
            text="Очистить",
            bg="black",
            fg="orange",
        )
        self.btn_save = Button(
            self,
            text="Сохранить в отд.файл",
            bg="black",
            fg="orange",
        )

        # demo widget
        self.btn_demo = Button(
            self,
            text="Демо",
            bg="black",
            fg="orange",
        )

        sort_types = [
            CATEGORY_ALL,
            ARTICLE_INCOME_NAME,
            ARTICLE_OUTLAY_NAME,
        ]
        sort_selection_type = StringVar(self)
        sort_selection_type.set(sort_types[0])
        self.menu_sort_types = OptionMenu(self, sort_selection_type, *sort_types)
        self.menu_sort_types.config(bg="black", fg="orange")
        self.menu_sort_types_in_menu = self.menu_sort_types.children["menu"]
        self.menu_sort_types_in_menu.bind(
            "<Leave>",
        )

        sort_categories = category_db.CategoryJSONManager.get_categories()
        sort_categories_names = []
        for _category in sort_categories:
            _category_name = _category.name
            sort_categories_names.append(_category_name)

        sort_categories.insert(0, CATEGORY_ALL)
        self.sort_selection_category = StringVar(self)
        self.sort_selection_category.set(sort_categories_names[0])
        self.menu_sort_categories = OptionMenu(
            self, self.sort_selection_category, *sort_categories_names
        )
        self.menu_sort_categories.config(bg="black", fg="orange")
        self.menu_sort_categories_in_menu = self.menu_sort_categories["menu"]
        self.menu_sort_categories_in_menu.bind(
            "<Leave>",
        )

        self.ent_sort_date_start = Entry(self, bg="black", fg="orange")
        self.ent_sort_date_end = Entry(self, bg="black", fg="orange")
        self.btn_sort_by_date = Button(
            self, text="Отсортировать", bg="black", fg="orange"
        )
        self.btn_sort_by_date.bind(
            "<Button-1>",
        )

    def __place_widgets(self):
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
        self.btn_save.place(
            relx=lbl_result_x,
            rely=btn_results_y,
            relwidth=result_widget_width,
            relheight=result_btn_height,
        )
