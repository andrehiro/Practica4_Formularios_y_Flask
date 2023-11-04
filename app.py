from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("public/index.html")
@app.route("/pagina1")
def pagina1():
    return render_template("public/pagina1.html")
@app.route("/pagina2")
def pagina2():
    return render_template("public/pagina2.html")
@app.route("/pagina3")
def pagina3():
    return render_template("public/pagina3.html")