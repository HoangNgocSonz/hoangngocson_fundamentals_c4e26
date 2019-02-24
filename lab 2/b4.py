from turtle import*
import b3
speed(0)
for i in range(200):
    b3.draw_square(i * 2, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

