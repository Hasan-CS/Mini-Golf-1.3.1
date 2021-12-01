# Made by Mohammed Jasim and Hasan Ahmad
# imports/basics
import turtle as trtl
import random as rand
wn = trtl.Screen()

# initialization
draw = trtl.Turtle()
ball = trtl.Turtle()
sand_one = trtl.Turtle()
sand_two = trtl.Turtle()
pond_one = trtl.Turtle()
pond_two = trtl.Turtle()
hole = trtl.Turtle()

wn.addshape("golf_ball.gif")
wn.addshape("pond.gif")
wn.addshape("sand.gif")
wn.addshape("hole.gif")

wn.bgcolor("#9BBC49")
wn.setup(800, 600)
draw.pensize(5)

map_list = ["m_one", "m_two", "m_three", "m_four"]

# fuctions
def draw_turtle(active_turtle, active_gif):
  active_turtle.shape(active_gif)
  wn.update()

def move(turtle, xx, yy):
    turtle.penup()
    turtle.goto(xx, yy)
    turtle.pendown()

def draw_map_one():
    pond_two.hideturtle()

    move(ball, -300, -200)
    move(hole, 300, 200)
    move(sand_one, 150, 50)
    move(sand_two, 50, -50)
    move(pond_one, 160, 200)
    move(draw, -320, -150)

    draw.fd(220)
    draw.lt(90)
    draw.fd(300)
    draw.rt(90)

    draw.fd(150)
    draw.lt(90)
    draw.fd(100)
    draw.rt(90)

    draw.fd(300)
    draw.rt(90)
    draw.fd(400)
    draw.rt(90)
    draw.fd(100)
    draw.lt(90)

    draw.fd(100)
    draw.rt(90)
    draw.fd(600)
    draw.rt(90)
    draw.fd(100)
    draw.rt(90)
    draw.fd(100)


# game
draw_turtle(ball, "golf_ball.gif")
draw_turtle(sand_one, "sand.gif")
draw_turtle(sand_two, "sand.gif")
draw_turtle(pond_one, "pond.gif")
draw_turtle(pond_two, "pond.gif")
draw_turtle(hole, "hole.gif")

draw_map_one()

wn.mainloop()