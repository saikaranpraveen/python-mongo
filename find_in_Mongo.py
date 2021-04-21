import pymongo
from pymongo import MongoClient


my_client = MongoClient("mongodb+srv://karansiamintern:1234@cluster0.4sl4c.mongodb.net/my_database?retryWrites=true&w=majority")

my_db = my_client["my_database"]
my_collection = my_db["my_collection"]



x = my_collection.find_one()

print(x)
