from turtle import*

def draw_star(x,y,length):
    up()
    goto(x,y)
    down()
    for i in range(5):
        fd(length)
        right(144)

