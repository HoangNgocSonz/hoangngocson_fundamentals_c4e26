from ex1 import db
import matplotlib.pyplot as plotter

js=db["customers"] 
list_even=js.find(
    {"ref":"events"}
)
list_ads=js.find(
    {"ref":"ads"}
)
list_wom=js.find(
    {"ref":"wom"}
)
print("events:",list_even.count())
print("ads:",list_ads.count())
print("wom:",list_wom.count())

pieLabels = 'event','ads','wom'
Share     = [list_even.count(),list_ads.count(),list_wom.count()]
figureObject, axesObject = plotter.subplots()
axesObject.pie(Share,
        labels=pieLabels,
        autopct='%1.2f',
        startangle=90)
plotter.show()