from ex4 import js

a=js.find(
    {
        "continent":"Africa",
    }
)
for i in a:
    print(i["name"])
