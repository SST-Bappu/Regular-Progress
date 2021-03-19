from flask import render_template,Flask,request,redirect,url_for
app=Flask(__name__)

           #methods=["POST","GET"])
@app.route("/login")
def login():
    #return render_template("index.html")
    return "<h1>It's working</h1>"
if __name__=="__main__":
    app.run(debug=True)