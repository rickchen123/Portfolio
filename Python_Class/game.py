# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle as t
import numpy as np
import random

## set screen
screen = t.Screen()
## set up background color
screen.bgcolor('black')
## set screen title
screen.title("Rick's Program")
##Change background pic(gif only)
screen.bgpic("kbgame-bg.gif")

screen.tracer(3)

## Draw Boundary
border = t.Turtle()
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pensize(3)
border.pendown()
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()


#set up player
player = t.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()

## set up Goals
num_goals = 10
goals = []

for count in range(num_goals):
    goals.append(t.Turtle())
    goals[count].color('red')
    goals[count].shape('circle')
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300)
                             ,random.randint(-300,300))
    
speed = 1
## Define Function
def turnleft():
    player.lt(30)

def turnright():
    player.rt(30)
def speed5():
    global speed
    speed = 5
def speed1():
    global speed
    speed = 1

def iscollision(t1,t2):
    d = np.sqrt((t1.xcor()-t2.xcor())**2
            +(t1.ycor()-t2.ycor())**2)
    if d<20:
        return True
    else:
        return False

##keyboard Binding
t.listen()
t.onkey(turnleft, 'Left')
t.onkey(turnright, 'Right')
t.onkeypress(speed5, 'Up')
t.onkeyrelease(speed1, 'Up')

#set score
score = 0
s = t.Turtle()
s.color('white')
s.hideturtle()

#set life
life = 3
l = t.Turtle()
l.color('white')
l.hideturtle()

while True:
    player.forward(speed)
    ## Boundary Checking
    if player.xcor()>300 or player.xcor()<-300:
        player.left(180)
        ## update life
        life = life - 1
        if life == 0:
            break  
        l.undo()
        l.penup()
        l.setposition(290,310)
        lifestring = 'Life: %s'%life
        l.write(lifestring,False, align = 'left', 
               font = ('Arial', 16,"normal"))
        
        
    if player.ycor()>300 or player.ycor()<-300:
        player.left(180)
        life = life - 1
        if life == 0:
            break
        l.undo()
        l.penup()
        l.setposition(290,310)
        lifestring = 'Life: %s'%life
        l.write(lifestring,False, align = 'left', 
               font = ('Arial', 16,"normal"))
       
    ## move goals
    for count in range(num_goals):
        goals[count].forward(3)
        if goals[count].xcor()>290 or goals[count].xcor()<-290:
            goals[count].left(180)
        
        if goals[count].ycor()>290 or goals[count].ycor()<-290:
            goals[count].left(180)
        
        ## Collision checking
        if iscollision(player, goals[count]):
            goals[count].setposition(random.randint(-300,300),
                                    random.randint(-300,300))
            goals[count].left(random.randint(0,360))
            
            #update score
            score = score + 1
            s.undo()
            s.penup()
            s.setposition(-290,310)
            scorestring = 'Score: %s'%score
            s.write(scorestring, False
                    , align = 'left'
                    ,font = ('Arial', 16,"normal"))

            
## Update Screen

screen.bgcolor('black')
final = t.Turtle()
final.hideturtle()
final.color('white')
end_string = 'You got %s points'%score
final.write(end_string, False, align = 'center'
            , font = ("Arial", 20, "normal"))
screen.exitonclick()