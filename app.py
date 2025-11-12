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



