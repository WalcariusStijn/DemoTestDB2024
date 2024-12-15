from repositories.ProductRepository import ProductRepository
from tabulate import tabulate 

class ProductServices:

    @staticmethod
    def print_products_from_category(parnumber: int) -> None:
        products = ProductRepository.load_products_from_category(parnumber)
        table = []
        for p in products :
            table.append([p.number, p.name, p.price, p.categorynumber])
        print(tabulate(table, headers = ["Number", "Name" , "Price Per Unit", "CategoryNumber"])) 

