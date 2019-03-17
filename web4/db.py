from pymongo import MongoClient
uri = "mongodb+srv://admin:admin14@cluster0-nydf8.mongodb.net/test?retryWrites=true"
#connect
client = MongoClient(uri)

#2.get database
db=client.test

# 3.get collection
# food_collection=db["ss"] #conllecton

# # 4> create a new document
# new_food = {
#     "name":"siêu bún chấm",
#     "price" : 22220,

# } #document
food_collection=db["food"]
user_collection=db["user"]
#5 insert new document into collection
# food_collection.insert_one(new_food)

#6.close connection
def close():
    client.close()