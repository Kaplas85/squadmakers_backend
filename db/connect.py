# Python
import os

# PyMongo
import pymongo

DB_URI = os.environ["DATABASE_URL"]

client = pymongo.MongoClient(DB_URI)

db = client["squadMakersDatabase"]
