from flask import Flask,render_template, request
app = Flask(__name__)

items=[
    {
        "name":"cơm rang",
        "price":25000
    },
    {
        "name":"bún đâu mắm tôm",
        "price":30000
    },
    {
        "name":"bún bò",
        "price":20000
    },
]

@app.route("/")
def menu():
    return render_template("menu.html",item_list=items, user = "son" )

@app.route("/food/<int:a>")
def food(a):
    return render_template("food_detail.html",item=items[a])

@app.route("/add_food",methods=["GET","POST"])
def add_food():
    if request.method =="GET":
        return render_template ("food_form.html")
    elif request.method =="POST":
        form = request.form
        n=form ["nam"]
        p=form ["price"]
        new_item={
            "name":n,
            "price":p,
        }
        items.append(new_item)
        return  n +" " +p+ "thanh cong"  #str(form) #"gui form ho, ok"
if __name__ == '__main__':
  app.run(debug=True)