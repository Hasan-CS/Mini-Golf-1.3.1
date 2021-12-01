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
sand_three = trtl.Turtle()
sand_four = trtl.Turtle()
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
    sand_three.hideturtle()
    sand_four.hideturtle()

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
    
    draw.hideturtle()

def draw_map_three():
    sand_three.hideturtle()
    sand_four.hideturtle()

    move(ball, 0, -200)
    move(hole, -300, 180)
    move(sand_one, 130, -15)
    move(sand_two, -20, 190)
    move(pond_one, 240, -200)
    move(pond_two, 0, -100)
    move(draw, -100, -250)

    draw.lt(90)
    draw.fd(200)
    for i in range(4):
        draw.lt(22.5)
        if i > 2:
            draw.fd(100)
        else:
            draw.fd(75)

    draw.rt(90)
    draw.fd(150)
    draw.rt(90)

    draw.fd(250)
    draw.rt(90)
    draw.fd(100)
    draw.bk(100)
    draw.lt(90)
    draw.fd(450)
    draw.rt(90)
    draw.fd(500)
    draw.rt(90)
    draw.fd(450)

    draw.rt(90)
    draw.fd(200)
    for i in range(4):
        draw.rt(22.5)
        if i > 2:
            draw.fd(100)
        else:
            draw.fd(75)

def draw_map_four():

    move(ball, 0, -100)
    move(hole, 0, 100)
    move(sand_one, 200, -40)
    move(sand_two, 70, 180)
    move(sand_three, -230, -100)
    move(sand_four, -100, 25)
    move(pond_one, -240, 180)
    move(pond_two, 240, -160)
    move(draw, 0, 0)


    draw.rt(45)
    for i in range(2):
        draw.fd(125)
        draw.bk(250)
        draw.fd(125)
        draw.rt(90)
    
    move(draw, -350, -220)
    draw.rt(45)
    for i in range(2):
        draw.fd(225)
        draw.rt(90)
        draw.fd(75)
        draw.bk(75)
        draw.lt(90)
        draw.fd(225)

        draw.rt(90)
        draw.fd(700)
        draw.rt(90)

# game
draw_turtle(ball, "golf_ball.gif")
draw_turtle(sand_one, "sand.gif")
draw_turtle(sand_two, "sand.gif")
draw_turtle(sand_three, "sand.gif")
draw_turtle(sand_four, "sand.gif")
draw_turtle(pond_one, "pond.gif")
draw_turtle(pond_two, "pond.gif")
draw_turtle(hole, "hole.gif")

#draw_map_one()
#draw_map_three()
#draw_map_four()

wn.mainloop()