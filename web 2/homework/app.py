from flask import Flask,render_template,request

app = Flask(__name__)

bike=[]

@app.route("/new_bike",methods = ["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike_form.html")
    elif request.method == "POST":
        form = request.form
        a=form["Model"]
        b=form["Daily"]
        c=form["Image"]
        d=form["Year"]
        new_bike={
            "Model":a,
            "Daily fee":b,
            "Image":c,
            "Year":d,
        }
        bike.append(new_bike)
        return "Model: "+ a +"\n"+",  Daily fee: "+ b+"\n" +",  Image: " +c+"\n" +",  Year: " +d
if __name__ == '__main__':
  app.run(debug=True)