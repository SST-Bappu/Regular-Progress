import mysql
from sql_connection import get_sql_connection
def get_all_products(connection):
        mycursor=connection.cursor()
        mycursor.execute("SELECT products.p_id, products.p_name,products.price_per_unit,uom.uom_name "
                         "FROM grocery_store.products inner join uom on uom.uom_id=products.uom_id")
        myresult=mycursor.fetchall()
        response=[]
        for row in myresult:
            response.append(
                row
            )
        return response
def insert_new_data(connection,product):
        mycursor = connection.cursor()
        query = ("INSERT INTO products "
                 "(p_name,uom_id,price_per_unit) "
                 "values(%s,%s,%s)")
        data = (product['p_name'],product['uom_id'],product['price_per_unit'])
        mycursor.execute(query, data)
        connection.commit()
        return mycursor.lastrowid
def delete_data(connection,product_id):
    mycursor=connection.cursor()
    mycursor.execute("DELETE FROM products WHERE p_id = %s", [product_id])
    print("1 item has been deleted successfully")
    connection.commit()


if __name__=="__main__":
    connection=get_sql_connection()
    product = {
        'p_name':'StickyNote',
        'uom_id':'1',
        'price_per_unit':'15'
    }
    #print(insert_new_data(connection, product))
    #delete_data(connection,12)
    products=get_all_products(connection)
    print(products)
    delete_data(connection,products[0][0])
    #print(products[0][0])
    for row in products:
        i = 0
        for cell in row:
            print(cell,end=" ")
        print(f"\n Got id = {row[0]}")


