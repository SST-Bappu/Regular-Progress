import mysql.connector
__mydb = None
def get_sql_connection():
    global __mydb
    if __mydb is None:
        __mydb = mysql.connector.connect(host="localhost", user="root", password="2267787",
                                       database='grocery_store')
    return __mydb