import turtle
import time
import random

delay=0.1

#this part is for the basic setup for the window of snakegame.
wn=turtle.Screen()
wn.title("Snake Game!")
wn.bgcolor("blue")
wn.setup(height=600,width=500)
wn.tracer(0)


#by this part we will create a head on the window.
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup
head.goto(0,0)
head.direction="left"








#this is the mainloop for screenupdate.

while True:
    wn.update()



wn.mainloop()