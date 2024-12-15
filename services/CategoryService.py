from models.Category import Category
from repositories.CategoryRepository import CategoryRepository
from tabulate import tabulate

class CategoryService:

    @staticmethod
    def print_all_categories():
        categories = CategoryRepository.get_all_categories()
        tabel = []
        for c in categories:
            tabel.append([c.number, c.name, c.description])
        print(tabulate(tabel, headers=["Nr","Naam","Beschrijving"]))

