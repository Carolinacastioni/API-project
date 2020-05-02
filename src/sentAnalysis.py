import pymongo
import re
from bson.json_util import dumps
from src.mongo import *
from src.errorHandler import errorHandler, Error404
from flask import Flask, request
from src.app import app
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")


#Get all the messages from a chat
def getChats(chatname):
    chat = db.find({"chat": chatname},{'_id':0, "quote":1})
    if not chat:
        return f"Error: This Chat doesn't exists"
    else:
        print("Success!")
        return dumps(chat)

#Analyze sentiment of a chat
def sentAnalysis(chatname):
    chatquotes = list(db.find({"chat": chatname},{"_id":0, "quote":1}))
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(str(chatquotes).strip('[]'))
    if sentiment["neg"] > sentiment["pos"]:
        return {"Score":sentiment, "Resume":"Mostly negative"}
    else:
        return {"Score":sentiment, "Resume":"Mostly positive"}