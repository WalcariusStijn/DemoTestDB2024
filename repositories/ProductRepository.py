from models.Product import Product
from repositories.Database import Database

class ProductRepository:

    @staticmethod
    def load_products_from_category(parcategorynr: int):
        results = []
        if not isinstance(parcategorynr, int):
            raise TypeError("No valid categorynumber, try again")
        
        #sql
        sql = "Select ProductNumber, ProductName, PricePerUnit From tblProducts WHERE categorynumber=%s"
        values=[parcategorynr]

        #execute
        list_dict = Database.get_rows(sql, values)
        if list_dict is not None:
            for dict_product in list_dict:
                try:
                    number = int(dict_product['ProductNumber'])
                    name = dict_product['ProductName']
                    price = float(dict_product['PricePerUnit'])
                    p = Product(number, name, price, parcategorynr)
                    results.append(p) 
                except Exception as ex:
                    print(ex)
        return results