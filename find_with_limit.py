import pymongo
from pymongo import MongoClient

my_client = MongoClient("mongodb+srv://karansiamintern:1234@cluster0.4sl4c.mongodb.net/my_database?retryWrites=true&w=majority")
my_db = my_client["my_database"]
my_collection = my_db["my_collection"]

my_result = my_collection.find().limit(5) #limits the results to 5

for x in my_result:
    print(x)