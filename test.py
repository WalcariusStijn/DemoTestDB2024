from repositories.Database import Database
from tabulate import tabulate
from services.CategoryService import CategoryService

# Test-connection database, first execute in a terminal window: pip install mysql-connector-python 
# rows = Database.get_rows("SELECT * FROM tblcategories")
# # print(rows)

# print(tabulate(rows, headers="keys"))

CategoryService.print_all_categories()

