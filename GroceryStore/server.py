from flask import Flask,render_template,request,redirect,url_for,flash
import products_dao
import sql_connection
import uom_dao
app=Flask(__name__)
app.secret_key= "hello"
connection=sql_connection.get_sql_connection()

@app.route("/index")
def index():
    global connection
    products = products_dao.get_all_products(connection)
    return render_template("table2.html",data=products)

@app.route("/delete_item/<string:id>")
def delete_item(id):
    global connection
    products_dao.delete_data(connection,id)
    flash('Product Deleted','alert')
    return redirect(url_for("index"))
@app.route("/new_order", methods=["POST","GET"])
def new_order():
    global connection
    products = products_dao.get_all_products(connection)
    return render_template("new_order.html",data=products)

@app.route("/add_new_item", methods=["POST","GET"])
def add_new_item():
    global connection
    uom = uom_dao.get_uom(connection)
    if request.method=="POST":
        if request.form.get("save"):
            result={
                'p_name': request.form["name"],
                'uom_id' : request.form["unit"],
                'price_per_unit' : request.form["price"]
                }
            products_dao.insert_new_data(connection,result)
            flash('1 Product has been inserted succefully','success')
            return redirect(url_for("index"))
        elif request.form.get("close"):
            return redirect(url_for("index"))
        else:
            return redirect(url_for("add_new_item"))
    return render_template("add_new_product.html", data=uom)



if __name__=="__main__":
    app.run(debug=True)