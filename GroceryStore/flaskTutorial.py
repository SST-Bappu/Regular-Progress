from flask import Flask, request, jsonify, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return "<h1>Yeap,</h1> <h2>I made it</h2>"
#@app.route("/<name>")
#def user(name):
 #   return f"<h1>Hello {name}!</h1>"
@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Admin!"))
@app.route("/<name>")
def index(name):
    #return render_template("index.html",content=name,r=2)
    return render_template("index.html", content=["Rahim","Karim","Jamal","Kamal"])
if __name__=="__main__":
    print("Starting python flask server for grocery management")
    app.run(port=5000)