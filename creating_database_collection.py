import pymongo
from pymongo import MongoClient

my_client = MongoClient("<url>")
my_db = my_client["my_database"]
my_collection = my_db["my_collection"]