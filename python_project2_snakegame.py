#python snake game this game is made by the owner of the utube channel tokyoEdtech
#this game is made using three useful python modules they are: turtle,time,random


#lets get started.
#setting up the screen
#part2: Snake head.
import sys
import playsound
import turtle
import time 
import random

delay=0.1

#score:
score=0
highscore=0


wn=turtle.Screen()
wn.title("Snake Game!")
wn.bgcolor("green")
wn.setup(height=600,width=600)
wn.tracer(0)  #turns off the screen updates.



#head of the snake part 2 

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#we are going to create food

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.goto(50,50)

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
# pen.write(f"Score:{score}    High Score:{highscore}  ",align="Center",font=("Courier",24,"normal"))

#body of the snake/bodygrow.

segments=[]


#function for snakemovement.

def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction!='up':
        head.direction='down'

def go_right():
    if head.direction!='left':
        head.direction='right'


def go_left():
    if head.direction!='right':
        head.direction='left'


#creating a function for move.

def move():

    if head.direction=="up":
        head.sety(head.ycor()+20)

    if head.direction=="down":
        head.sety(head.ycor()-20)

    if head.direction=="right":
        head.setx(head.xcor()+20)

    if head.direction=="left":
        head.setx(head.xcor()-20)



# for keyboard binding.

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loop

while True:
    wn.update()

    #check for the collision of the snake with the boarder.
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.0001)
        head.goto(random.randint(-290,290),random.randint(-290,290))
        head.direction="stop"

        #hiding the segments:

        for segment in segments:
            segment.goto(1000,1000)


        segments.clear()
        score=0
        pen.clear()
        pen.write(f"Score:{score}    High Score:{highscore}  ",align="Center",font=("Courier",24,"normal"))
 
    
    
#checking for the collision of the snake with the food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #after the collision new segment of the part of the snake to be added to the body,

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        #score addition.
        score=score+1
        if score>highscore:
            highscore=score
        
        pen.clear()
        pen.write(f"Score:{score}    High Score:{highscore}  ",align="Center",font=("Courier",24,"normal"))

        

    #move the last segment of the body with head

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move the segment 0 to the position of the head.

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)



    move()

    
      #check for the body collision:
    for segment in segments:
        if segment.distance(head)<15:
            time.sleep(0.0001)
            head.goto(random.randint(-290,290),random.randint(-290,290))
            head.direction="stop"
            #hiding the segments:

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()  
            #reset the score:
            score=0
            pen.clear()
            pen.write(f"Score:{score}    High Score:{highscore}  ",align="Center",font=("Courier",24,"normal"))
  

    time.sleep(delay)
wn.mainloop()