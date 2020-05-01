from src.config import PORT
from src.app import app
from flask import Flask, request
import src.mongo 
from src.errorHandler import errorHandler

@app.route("/user/<name>")
@errorHandler
def getname(name):
    nombre = getUser(name)
    return nombre

#Create a user
@app.route("/user/create/<username>")
@errorHandler
def createUser(username):
    usuario = createUsername(username)
    return usuario

app.run("0.0.0.0", PORT, debug=True)