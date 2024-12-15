class Product:
    def __init__(self, par_number, par_name, par_price, par_categorynumber):
        self.number = par_number
        self.name = par_name
        self.categorynumber = par_categorynumber
        self.price = par_price

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
            raise ValueError("No valid number")

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> str:
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        self.__name = value
    
    # ********** property categorynumber - (setter/getter) ***********
    @property
    def categorynumber(self) -> int:
        """ The categorynumber property. """
        return self.__categorynumber
    
    @categorynumber.setter
    def categorynumber(self, value: int) -> None:
        if isinstance(value, int):
            self.__categorynumber = value
        else:
            raise ValueError("No valid categorynumber")
    
    # ********** property price - (setter/getter) ***********
    @property
    def price(self) -> float:
        """ The price property. """
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        if isinstance(value, float):
            self.__price = value
        else:
            raise ValueError("No valid price")
    


    def __str__(self):
        return f"output :{self.number} {self.name} {self.categorynumber} {self.price} "
    
    def __repr__(self):
        return f"{self.name} "