from flask import Flask,render_template, request
import food

app = Flask(__name__)

@app.route("/food/list")
def menu():
  all_food = food.get({})
  return render_template("food_list.html",f_list= all_food )

@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return render_template("food_id.html",f=f)
    

@app.route("/food/add",methods=["GET","POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_add.html" )
    elif  request.method == "POST":
        form = request.form
        n=form["name"]
        p=form["price"]
        food.add_new(n,p)
        return render_template("food_add.html" )

if __name__ == '__main__':
  app.run(debug=True)