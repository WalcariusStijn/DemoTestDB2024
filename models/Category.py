from typing import List
from models.Product import Product

class Category:

    def __init__(self, parnumber, parname, pardescription):
        self.number = parnumber
        self.name = parname
        self.description = pardescription
        self.__products = []

    # ********** property products - (getter only) ***********
    @property
    def products(self) -> list[Product]:
        """ The products property. """
        return self.__products
    
    
    def voeg_product_toe(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)


    # ********** property number - (setter/getter) ***********
    @property
    def number(self) -> int:
        """ The number property. """
        return self.__number
    
    @number.setter
    def number(self, value: int) -> None:
        if isinstance(value, int):
            self.__number = value
        else:
            raise ValueError("No valid categorynumber")
    
    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> str:
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("No valid name")
    
    # ********** property description - (setter/getter) ***********
    @property
    def description(self) -> str:
        """ The description property. """
        return self.__description
    
    @description.setter
    def description(self, value: str) -> None:
        if isinstance(value, str):
            self.__description = value
        else:
            raise ValueError("No valid description")

    def __str__(self):
        return f"\n{self.number}\t\t{self.name} \t\t{self.description}  "
    
    def __repr__(self):
        return f"{self.name}"
    