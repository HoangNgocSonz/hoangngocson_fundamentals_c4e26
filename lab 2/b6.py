from turtle import*
import b5
speed(0)
color("red")
for j in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    b5.draw_star(x, y, length)
    if(j==0): print (x,y)


