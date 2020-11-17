import json
from settings import DEFAULT_CATEGORIES_LIST
from category import Category


class CategoryJSONManager:
    @classmethod
    def save_category(cls, category):
        cls.save_categories([category])

    @classmethod
    def save_categories(cls, categories):
        categories_list = cls.get_categories()
        categories_list.extend(categories)

        categories_names_list = []
        for _category in categories_list:
            _category_name = _category.name
            categories_names_list.append(_category_name)

        with open(
            "categories_list.json", "w", encoding="utf-8"
        ) as file_with_categories:
            json.dump(categories_names_list, file_with_categories, ensure_ascii=False)

    @staticmethod
    def get_categories():
        try:
            with open("categories_list.json", encoding="utf-8") as file_with_categories:
                categories_names_list = json.load(file_with_categories)
        except FileNotFoundError:
            categories_names_list = DEFAULT_CATEGORIES_LIST

        categories_list = []
        for _category_name in categories_names_list:
            category = Category(_category_name)
            categories_list.append(category)

        return categories_list

    @classmethod
    def delete_category(cls, category):
        categories_list = cls.get_categories()
        del categories_list[category]

        cls.__write_categories(categories_list)

    @staticmethod
    def __write_categories(categories_list):
        categories_names_list = []
        for _category in categories_list:
            _category_name = _category.name
            categories_names_list.append(_category_name)

        with open(
            "categories_list.json", "w", encoding="utf-8"
        ) as file_with_categories:
            json.dump(categories_names_list, file_with_categories, ensure_ascii=False)
