from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<weight>/<height>")
def bmi(weight,height):
    bmi=int(weight)/(int(height)*int(height)/10000)
    if bmi<16:
        b= "BMI: "+str(round(bmi,1)) +" --> "+"Severely underweight" 
    elif 16<=bmi<18.5:
        b= "BMI: "+str(round(bmi,1)) +" --> "+"Underweight"        
    elif 18.5<=bmi<25:
        b= "BMI: "+str(round(bmi,1)) +" --> "+"Normal"      
    elif 25<=bmi<30:
        b= "BMI: "+str(round(bmi,1)) +" --> "+"Overweight"
    else:
        b= "BMI: "+str(round(bmi,1)) +" --> "+"Obese"
    return b
if __name__ == '__main__':
  app.run(debug=True)
