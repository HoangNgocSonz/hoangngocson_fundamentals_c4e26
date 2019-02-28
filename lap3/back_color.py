from random import *
from random import randint,choice

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes

def generate_quiz():
    li=["red","blue","green","yellow"]
    mean =choice(li)

    lis=['#C62828',"#4CAF50","#FFD600","#3F51B5"]
    color=choice(lis)
    
    return [
                mean,
                color,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if (20<=x<=120)and(60<=y<=160):
            if text == "blue":
                return True
            else:
                return False
        if (140<=x<=240)and(60<=y<=160):
            if text == "red":
                return True
            else:
                return False
        if (20<=x<=120)and(180<=y<=280):
            if text == "yellow":
                return True
            else:
                return False
        if (140<=x<=240)and(180<=y<=280):
            if text == "green":
                return True
            else:
                return False

    if quiz_type == 1:
        if (20<=x<=120)and(60<=y<=160):
            if color == "#3F51B5":     # blue
                return True
            else:
                return False
        if (140<=x<=240)and(60<=y<=160):
            if color == "#C62828":  # red
                return True
            else:
                return False
        if (20<=x<=120)and(180<=y<=280):
            if color == "#FFD600": #YELLOW
                return True
            else:
                return False
        if (140<=x<=240)and(180<=y<=280):
            if color == "#4CAF50":# green
                return True
            else:
                return False

   