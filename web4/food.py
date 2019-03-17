from db import food_collection,user_collection
from bson import ObjectId

def add_new(name,price):
    new_food={
        "name":name,
        "price":price,
    }
    food_collection.insert_one(new_food)

def get(query):
    food_list = food_collection.find_one(query)
    return food_list

def get_by_id(id):
    f=food_collection.find_one({'_id': ObjectId(id)})
    return f

def delete_by_id(id):
    food_collection.delete_one({'_id': ObjectId(id)})

def update_by_id(id,name,price):
    query={'_id': ObjectId(id)}
    update = { "$set":{"name":name},
            "$set":{"price":price},
     }
    food_collection.find_one_and_update(query,update)

def add(username,password):
    new={
        "USERNAME":username,
        "PASSWORD":password,
    }
    user_collection.insert_one(new)


def find_by_username(username):
    info = user_collection.find_one({"USERNAME":username})
    return info

if __name__=="__main__":
    add("vegeta","bunmas123")
    # a=find_by_username("songoku")
    # print(a)
    # food_collection.delete_one({'_id': ObjectId('5c81252797eba70d20a38bad')})
    # delete_by_id('5c8a537f97eba737480d01d2')
    # f=get_by_id('5c8a537f97eba737480d01d2')
    # if f != None:
    #     print (f["name"])
    # else:
    #     print ("not found")
    # query={'_id': ObjectId('5c812ade97eba73c68e24c1d')}
    # update = { "$set":{"price":10000} }#$inc: tang, $dec:giam, $set,$unset
    # food_collection.find_one_and_update(query,update)
    # print (*get({'_id': ObjectId('5c812ade97eba73c68e24c1d')}))
   
        
