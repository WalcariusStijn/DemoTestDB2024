from models.Category import Category
from repositories.CategoryRepository import CategoryRepository
from repositories.ProductRepository import ProductRepository
from tabulate import tabulate

class CategoryService:

    @staticmethod
    def print_all_categories():
        categories = CategoryRepository.get_all_categories()
        tabel = []
        for c in categories:
            tabel.append([c.number, c.name, c.description])
        print(tabulate(tabel, headers=["Nr","Naam","Beschrijving"]))


    @staticmethod
    def print_all_categories_with_products():
        categories = CategoryRepository.get_all_categories()
        for cat in categories:
            products = ProductRepository.load_products_from_category(cat.number)
            for p in products:
                cat.voeg_product_toe(p)
        tabel = []
        for c in categories:
            tabel.append([c.name, len(c.products)])
        print(tabulate(tabel, headers=["Name", "Number of Products"]))

    @staticmethod
    def add_category(name: str, description: str):
        try:
            new_category = Category(0, name, description)
            new_category = CategoryRepository.create(new_category)
            print(f"Categorie {new_category.name} was created with id {new_category.number}")
        except Exception as ex:
            print(ex)