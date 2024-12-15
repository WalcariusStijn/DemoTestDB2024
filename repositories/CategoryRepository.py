from models.Category import Category
from repositories.Database import Database

class CategoryRepository:

    @staticmethod
    def get_all_categories() -> list[Category]:
        result = []
        #1 build sql-string
        sql = "Select * From tblcategories"

        #execute sql-string
        list_dict = Database.get_rows(sql)
        if list_dict is not None:
            for dict_category in list_dict:
                try:
                    nr = dict_category["CategoryNumber"]
                    name = dict_category["CategoryName"]
                    description = dict_category["Description"]
                    cat = Category(nr, name, description )
                    result.append(cat)
                except Exception as ex:
                    print(ex)
        return result

    @staticmethod
    def create(new_cat: Category):
        #sql
        sql = "insert into tblCategories (CategoryName, Description) Values (%s,%s)"
        values = [new_cat.name, new_cat.description]
        new_cat_nr = Database.execute_sql(sql,values)

        if new_cat_nr is not None:
            new_cat.number = new_cat_nr
            return new_cat
        else:
            return None
