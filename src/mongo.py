from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
from src.errorHandler import errorHandler, Error404
from flask import Flask, request
from src.app import app
import re

client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["quotes"]

@app.route("/user/<name>")
@errorHandler
def getUser(name):
    namereg = re.compile(f"^{name}", re.IGNORECASE)
    user = db.find({"user":namereg},{"_id":0, "user":1, "quote":1, "chat":1})
    print(f"user: {namereg}")
    x = dumps(user)
    if len(x) < 3:
        print("ERROR")
        raise Error404("user not found")
    print("OK")
    print(len(x))
    return x