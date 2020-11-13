"""file for main_window control"""
from tkinter import (
    Tk,
    Frame,
    Button,
    Entry,
    Label,
    Listbox,
    OptionMenu,
    StringVar,
    Scrollbar,
    RIGHT,
    BOTH,
)
import settings


class Application:
    """control app"""
    def __init__(self):
        """create main_window"""
        self.main_window = Tk()

    def start(self):
        """start app"""
        self.main_window.mainloop()

    def stop(self):
        """stop app"""
        self.main_window.destroy()


class Window(Application):
    """control main_window"""
    def __init__(self):
        super().__init__()

        self.__configure_window()

    def __configure_window(self):
        """configure main_window"""
        self.main_window.title("FinanceControl")
        self.main_window.config(bg="grey")


class WindowFrames(Window):
    """control frames"""
    def __init__(self):
        """create frames for main_window"""
        super().__init__()

        self.frame_left = Frame(self.main_window, bg="orange")
        self.frame_right = Frame(self.main_window, bg="orange")

        self.__place_frame()

    def __place_frame(self):
        """pack frames"""
        self.frame_left.place(relx=0.01, rely=0.01, relwidth=0.485, relheight=0.98)
        self.frame_right.place(relx=0.505, rely=0.01, relwidth=0.485, relheight=0.98)


class FrameWidgets(WindowFrames):
    """control widgets for main _window frames"""
    def __init__(self):
        """create widgets"""
        super().__init__()

        # widgets for income and outlay
        self.lbl_name = Label(
            self.frame_left, text="Введите название:", bg="black", fg="orange"
        )
        self.ent_name = Entry(self.frame_left, bg="black", fg="orange")
        self.lbl_sum = Label(
            self.frame_left, text="Введите сумму:", bg="black", fg="orange"
        )
        self.ent_sum = Entry(self.frame_left, bg="black", fg="orange")
        self.btn_income = Button(
            self.frame_left,
            name="income",
            text="Добавить доход",
            bg="black",
            fg="orange",
        )
        self.btn_outlay = Button(
            self.frame_left,
            name="outlay",
            text="Добавить расход",
            bg="black",
            fg="orange",
        )

        # widget for demo
        self.btn_demo = Button(self.frame_left, text="Демо", bg="black", fg="orange")

        # widgets for results
        self.box_result = Listbox(self.frame_right, bg="black", fg="orange")
        self.sb_result = Scrollbar(self.box_result, bg="black")

        self.sb_result.pack(side=RIGHT, fill=BOTH)
        self.box_result.config(yscrollcommand=self.sb_result.set)
        self.sb_result.config(command=self.box_result.yview)

        self.lbl_incomes = Label(self.frame_right, bg="black", fg="green")
        self.lbl_outlays = Label(self.frame_right, bg="black", fg="red")
        self.lbl_result = Label(self.frame_right, bg="black", fg="orange")

        self.btn_del = Button(self.frame_right, text="Удалить", bg="black", fg="orange")
        self.btn_clean_box = Button(
            self.frame_right, text="Очистить", bg="black", fg="orange"
        )
        self.btn_save = Button(
            self.frame_right, text="Сохранить в отд.файл", bg="black", fg="orange"
        )

        # widgets for categories
        self.lbl_category = Label(
            self.frame_left, text="Выберите категорию:", bg="black", fg="orange"
        )

        self.categories = settings.DEFAULT_CATEGORIES_LIST
        self.selection_category = StringVar(self.frame_left)
        self.selection_category.set(self.categories[0])
        self.menu_categories = OptionMenu(
            self.frame_left, self.selection_category, *self.categories
        )
        self.menu_categories.config(bg="black", fg="orange")

        self.btn_categories = Button(self.frame_left, text="+", bg="black", fg="orange")

        # widgets for sorting
        self.sort_types = [
            settings.CATEGORY_ALL,
            settings.ARTICLE_INCOME_NAME,
            settings.ARTICLE_OUTLAY_NAME,
        ]
        self.sort_selection_type = StringVar(self.frame_right)
        self.sort_selection_type.set(self.sort_types[0])
        self.menu_sort_types = OptionMenu(
            self.frame_right, self.sort_selection_type, *self.sort_types
        )
        self.menu_sort_types.config(bg="black", fg="orange")
        self.menu_sort_types_in_menu = self.menu_sort_types.children["menu"]
        self.menu_sort_types_in_menu.bind("<Leave>")

        self.sort_categories = settings.DEFAULT_CATEGORIES_LIST
        self.sort_categories.insert(0, settings.CATEGORY_ALL)
        self.sort_selection_category = StringVar(self.frame_right)
        self.sort_selection_category.set(self.sort_categories[0])
        self.menu_sort_categories = OptionMenu(
            self.frame_right, self.sort_selection_category, *self.sort_categories
        )
        self.menu_sort_categories.config(bg="black", fg="orange")
        self.menu_sort_categories_in_menu = self.menu_sort_categories["menu"]
        self.menu_sort_categories_in_menu.bind("<Leave>")

        self.ent_sort_date_start = Entry(self.frame_right, bg="black", fg="orange")
        self.ent_sort_date_end = Entry(self.frame_right, bg="black", fg="orange")
        self.btn_sort_by_date = Button(
            self.frame_right, text="Отсортировать", bg="black", fg="orange"
        )
        self.btn_sort_by_date.bind("<Button-1>")

        self.__place_widgets()

    def __place_widgets(self):
        """pack widgets"""
        # frame_left
        self.lbl_name.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.05)
        self.ent_name.place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.05)
        self.lbl_sum.place(relx=0.01, rely=0.13, relwidth=0.98, relheight=0.05)
        self.ent_sum.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.05)
        self.lbl_category.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.05)
        self.menu_categories.place(relx=0.01, rely=0.31, relwidth=0.7, relheight=0.05)
        self.btn_categories.place(relx=0.72, rely=0.31, relwidth=0.27, relheight=0.05)
        self.btn_income.place(relx=0.01, rely=0.38, relwidth=0.48, relheight=0.1)
        self.btn_outlay.place(relx=0.51, rely=0.38, relwidth=0.48, relheight=0.1)
        self.btn_demo.place(relx=0.01, rely=0.49, relwidth=0.48, relheight=0.1)

        # frame_right
        self.menu_sort_types.place(relx=0.01, rely=0.01, relwidth=0.2, relheight=0.05)
        self.menu_sort_categories.place(
            relx=0.22, rely=0.01, relwidth=0.2, relheight=0.05
        )
        self.ent_sort_date_start.place(
            relx=0.43, rely=0.01, relwidth=0.2, relheight=0.05
        )
        self.ent_sort_date_end.place(relx=0.63, rely=0.01, relwidth=0.2, relheight=0.05)
        self.btn_sort_by_date.place(relx=0.84, rely=0.01, relwidth=0.15, relheight=0.05)
        self.box_result.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.6)
        self.lbl_incomes.place(relx=0.01, rely=0.67, relwidth=0.32, relheight=0.06)
        self.lbl_outlays.place(relx=0.34, rely=0.67, relwidth=0.32, relheight=0.06)
        self.lbl_result.place(relx=0.67, rely=0.67, relwidth=0.32, relheight=0.06)
        self.btn_del.place(relx=0.01, rely=0.73, relwidth=0.32, relheight=0.1)
        self.btn_clean_box.place(relx=0.34, rely=0.73, relwidth=0.32, relheight=0.1)
        self.btn_save.place(relx=0.67, rely=0.73, relwidth=0.32, relheight=0.1)
