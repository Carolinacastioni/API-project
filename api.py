from src.config import PORT
from src.app import app
from flask import Flask, request
from src.mongo import *
from src.errorHandler import errorHandler
from src.sentAnalysis import *
from src.recommender import recommendUser

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
    return grupo

#Add user to a chat
@app.route("/chat/<chatname>/adduser/<username>")
@errorHandler
def adduser(chatname, username):
    add_users = addUser(chatname, username)
    return add_users

#Add message to a chat
@app.route("/chat/<chatname>/user/<username>/addmessage/<message>")
@errorHandler
def addmessage(chatname, username, message):
    add_message = addMessage(chatname, username, message)
    return add_message

#Get all the messages from a chat
@app.route("/chat/<chatname>/list")
@errorHandler
def getchats(chatname):
    gc = getChats(chatname)
    return gc

#Analyze sentiment of a chat
@app.route("/chat/<chatname>/sentiment")
@errorHandler
def sentanalysis(chatname):
    sentiments = sentAnalysis(chatname)
    return sentiments

#Recommend friends based on sentiments
@app.route("/user/<username>/recommend")
@errorHandler
def recommenduser(username):
    recommendation = recommendUser(username)
    return recommendation

app.run("0.0.0.0", PORT, debug=True)