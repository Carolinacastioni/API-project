from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
from src.errorHandler import errorHandler, Error404
from flask import Flask, request
from src.app import app
import re

#Conect to Mongodb
client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()["quotes"]

#Create users and save into DB
def createUsername(username):
    usernames = (db.distinct("user"))
    if username in usernames:
        userex = db.find({"user":username})
        return {"Error":"This User already exists", "info":dumps(userex)}
    else:
        db.insert_one({"user": username})
        newuser = db.find({"user":username})
        return {"Ok":"New user was created", "info":dumps(newuser)}
    
#Create chats and save into DB
def createChats(chatname):
    chats = (db.distinct("chat"))
    if chatname in chats:
        return f"Error: This Chat already exists"
    else:
        db.insert_one({"chat": chatname})
        return f"New chat was created"

#Add a user to a chat
def addUser(chatname, username):
    queryuser = db.find({"user": username},{'_id':0})
    if queryuser.count() == 0:
        return f"Error: This user doesn't exist."
    else:
        query = db.find({"$and":[{"user": username},{"chat": chatname}]},{'_id':0})
        if query.count() == 0:
            db.update({"chat":chatname},{"$push":{"user":username}})
            return f"Great! The user were added to the chat."
        else:
            return f"This is already in the chat."

