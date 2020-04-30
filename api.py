from src.config import PORT
from src.app import app
from flask import Flask, request
import src.mongo 
import src.errorHandler

@app.route("/hola")
def basicResponse():
    return 'Hello, World!'



app.run("0.0.0.0", PORT, debug=True)