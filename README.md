![]()

# Project | Chat Sentiment Analysis

## Introduction

In this project we will create an API to store chat messages and users in a Mongodb database. After we will analyze the sentiment of the chats as Positive, Negative or Neutral.  Finally, we will recommend the top three friends to a user based on the sentiment similarity. Please find below the details about the project. 

## Mongo.py

In this file, we have created an API in Flask. Please find the API endpoints below:

  USER - Endpoints:
- Create users and save into the Mongodb database: Project-API.quotes

  CHAT - Endpoints:
- Create chats and save into the database: TVShows, Party, Ironhack, Fitness, Cooking.
- Add users into the chats. Six users per chat.
- Add a message to the chats. One per user. 

## SentAnalysis.py

Here is the sentiment analysis of each chat.

- Get all the messages from a chat. 
   
- Analyze the sentiment of the messages on the chat
  Classify them into Mostly Positive or Mostly Negative and show the details, by using the NLTK sentiment analysis package.
  
## Recommender.py

This section is for recommend the top three friends of a user based on the sentiment similarity.

- Recommending friends using a recommender system with NLP analysis.

## Links

- [<https://www.nltk.org/]>
- [<https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]>
- [<https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]>