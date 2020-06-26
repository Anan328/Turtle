
import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
t.color("red")
colors=["yellow","green","black","brown","orange","pink"]
t.pensize(5)
def up():
    t.setheading(90)
    t.forward(100)
def down():
    t.setheading(270)
    t.forward(100)
def left():
    t.setheading(180)
    t.forward(100)
def right():
    t.setheading(0)
    t.forward(100)
def click(x,y):
    t.color(random.choice(colors))
turtle.listen()
turtle.onkey(up,"w")
turtle.onkey(down,"s")
turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.onscreenclick(click,3)
turtle.mainloop()