from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
from src.errorHandler import errorHandler, Error404

client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["api-project.quotes"]

@app.route("/chat/<id>")
@errorHandler
def getChat(id):
    id = db.find({"chat":id},{"_id":0, "user":1, "quote":1, "chat":1})
    print(f"chat: {id}")
    if not id:
        print("ERROR")
        raise Error404("chat not found")
    print("OK")
    return dumps(id)