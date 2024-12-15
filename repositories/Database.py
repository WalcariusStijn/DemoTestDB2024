from mysql import connector  #pip install mysql-connector-python 
import os


class Database:

    #region 1. open connection
    @staticmethod
    def __open_connection():
        try:
            db = connector.connect(
                option_files=os.path.abspath(os.path.join(
                    os.path.dirname(__file__), "../config.py")),
                autocommit=False
            )
            if "AttributeError" in(str(type(db))):
                raise Exception("Wrong values in config-file")
            cursor = db.cursor(
                dictionary=True, buffered=True)  # lazy loaded
            return db, cursor
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: no connection with the database")
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print("Error: the database is not founded")
            else:
                print(err)
            return
    #endregion

    #region 2. Executes READS
    @staticmethod
    def get_rows(sqlQuery, params=None):
        result = None
        db, cursor = Database.__open_connection()
        try:

            cursor.execute(sqlQuery, params)

            result = cursor.fetchall()
            cursor.close()
            if (result is None):
                print(ValueError(f"No results found.[DB Error]"))
            db.close()
        except Exception as error:
            print(error)  # development boodschap
            result = None
        finally:
            return result

    @staticmethod
    def get_one_row(sqlQuery, params=None):
        db, cursor = Database.__open_connection()
        try:
            cursor.execute(sqlQuery, params)
            result = cursor.fetchone()
            cursor.close()
            if (result is None):
                raise ValueError("No resultst found.[DB Error]")
        except Exception as error:
            print(error)  # development boodschap
            result = None
        finally:
            db.close()
            return result
    #endregion

    #region 3. Executes INSERT, UPDATE, DELETE with PARAMETERS
    @staticmethod
    def execute_sql(sqlQuery, params=None):
        result = None
        db, cursor = Database.__open_connection()
        try:
            cursor.execute(sqlQuery, params)
            db.commit()
            result = cursor.lastrowid
            if result != 0:  # succesfull create statement
                result = result
            else:  
                if cursor.rowcount == -1:  # Wrong SQL command
                    raise Exception("Error in SQL")
                elif cursor.rowcount == 0:  # no changes detected
                    result = 0
                elif result == "undefined":  # Wrong SQL Command
                    raise Exception("SQL error")
                else:
                    result = cursor.rowcount    # succesfull delete/update statement
        except connector.Error as error:
            db.rollback()
            result = None
            print(f"Error: Data not saved.{error.msg}")
        finally:
            cursor.close()
            db.close()
            return result
    #endregion
