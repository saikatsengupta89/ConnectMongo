import pandas as pd
from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'temp'
COLLECTION_NAME = 'posts'
connection= MongoClient (MONGODB_HOST, MONGODB_PORT)
collection= connection[DB_NAME][COLLECTION_NAME]

# make an API call to the MongoDB server using a Collection object
cursor= collection.find()

# get all the documents inside a collection as a list of dictionaries
mongo_docs= list(cursor)

# create an empty DataFrame obj for storing Series objects
docs = pd.DataFrame(columns=[])
for num,doc in enumerate (mongo_docs):
    # convert ObjectId() to str
    doc["_id"] = str(doc["_id"])
    # get document _id from dict
    doc_id = doc["_id"]
    # create a Series obj from the MongoDB dict
    series_obj = pd.Series(doc, name=doc_id)
    # append the MongoDB Series obj to the DataFrame obj
    docs = docs.append(series_obj)


# export MongoDB documents to a CSV file
docs.to_csv("C:/PycharmProjects/ConnectMongo/posts.csv", ",")