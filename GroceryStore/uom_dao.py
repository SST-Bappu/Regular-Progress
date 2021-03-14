from sql_connection import get_sql_connection
import mysql
def get_uom(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * from uom")
    result=cursor.fetchall()
    return result


if __name__=="__main__":
    connection=get_sql_connection()
    uom=get_uom(connection)
    for i,unit in uom:
        print(f"This ID-{i} and this is the value- {unit}")