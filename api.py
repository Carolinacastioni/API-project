from src.config import PORT
from src.app import app
from flask import Flask, request
from src.mongo import *
from src.errorHandler import errorHandler

#Create users
@app.route("/user/create/<username>")
@errorHandler
def createUser(username):
    usuario = createUsername(username)
    return usuario

#Create chats
@app.route("/chat/create/<chatname>")
@errorHandler
def createchat(chatname):
    grupo = createChats(chatname)
    print(grupo)
    return grupo

#Add user to a chat
@app.route("/chat/<chatname>/adduser/<username>")
@errorHandler
def adduser(chatname, username):
    add_users = addUser(chatname, username)
    print(add_users)
    return add_users

app.run("0.0.0.0", PORT, debug=True)