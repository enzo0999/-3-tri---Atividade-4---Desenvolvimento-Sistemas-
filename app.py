from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Flask !!</h1>"

@app.route("/versao")
def versao():
    versao = "1.1.0"
    return f"App v{versao}"


@app.route("/saudar/<nome>")
def saudar(nome):
    nome = nome.capitalize()
    return f"Olá, {nome}!"


@app.route("/quadrado/<int:n>")
def quadrado(n):
    resultado = n * n
    return f"{n}² = {resultado}"


@app.route("/home")
def home():
    return redirect("/")


@app.route("/pagina")
def pagina():
    return render_template("pagina.html")


@app.route("/buscar/<item>")
def buscar(item):
    itens = ["maçã", "laranja", "banana", "uva"]
    if item in itens:
        return f"Item '{item}' encontrado!"
    else:
        return f"Item '{item}' não encontrado!"

if __name__ == "__main__":
    app.run(debug=True)
