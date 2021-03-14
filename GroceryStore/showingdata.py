from flask import Flask,render_template,request
import products_dao
import sql_connection
app=Flask(__name__)
connection=sql_connection.get_sql_connection()
products = products_dao.get_all_products(connection)
@app.route("/index")
def table():
    return render_template("index.html",data=products)

if __name__=="__main__":
    app.run(debug=True)