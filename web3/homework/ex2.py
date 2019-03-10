from ex1 import js

def add_new(t,a,c):
    new = {
    "title":t,
    "author":a,
    "content":c,
    }
    js.insert_one(new)

add_new("ninja","Sơn Hoàng","Naruto Uzumaki")