from ex4 import js

a=js.find(
    {
        "continent":"S. America",
        "length":{"$lte":1000}
    }
)
for i in a:
    print(i["name"])