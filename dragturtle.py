# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:19:44 2020

@author: ANAN SHAH
"""

import turtle
import random
s=turtle.Screen()
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.color("red")
t.pensize(5)
colors=["green","blue","yellow","orange","brown","purple","red","cyan","black","grey"]
def drag(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(drag)
def penup():
    t.penup()
def pendown():
    t.pendown()
def clean():
    t.clear()
def paint(x,y):
    t.color(random.choice(colors))
turtle.listen()
turtle.ondrag(drag)
turtle.onkey(penup,"z")
turtle.onkey(pendown,"x")
turtle.onscreenclick(paint,3)
turtle.onkey(clean,"c")
s.mainloop()
