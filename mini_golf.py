# Made by Mohammed Jasim and Hasan Ahmad
# imports/basics
import turtle as trtl
import random as rand
wn = trtl.Screen()

### initialization
greeting = wn.textinput("Welcome to Golf Game!", "Use the user inputs to move the ball and click the ball to reset it! Type 'ok' to begin: ")

# Creation of all the objects(turtles) in the game
draw = trtl.Turtle()
ball = trtl.Turtle()
sand_one = trtl.Turtle()
sand_two = trtl.Turtle()
sand_three = trtl.Turtle()
sand_four = trtl.Turtle()
pond_one = trtl.Turtle()
pond_two = trtl.Turtle()
hole = trtl.Turtle()

# All game images - this section also sets up background color, sizes and speed
wn.addshape("golf_ball.gif")
wn.addshape("pond.gif")
wn.addshape("sand.gif")
wn.addshape("hole.gif")

wn.bgcolor("#9BBC49")
wn.setup(800, 600)

draw.speed(7)
draw.pensize(5)
ball.speed(2)

# Different maps list + variable that stores a random map
map_list = ["m_one", "m_two", "m_three", "m_four"]
which_map = rand.choice(map_list)

# countdown setup (variables required for the timer to work)
font_setup = ("Arial", 20, "normal")
timer = 100
counter_interval = 1000   
timer_up = False

# setting up the countdown turtle
counter = trtl.Turtle()
counter.color("white")
counter.penup()
counter.goto(-300, 255)

### fuctions
# this is the function used when the ball is clicked on, it returns to the starting spot based on which map is chosen
def return_home(x, y):
    global which_map
    if which_map == "m_one":
        move(ball, -300, -200)
    if which_map == "m_two":
         move(ball, 250, 300)
    if which_map == "m_three":
        move(ball, 0, -200)
    if which_map == "m_four":
        move(ball, 0, -100)

# this is a basic function taking a turtle and image as parameters, and attaches them together
def draw_turtle(active_turtle, active_gif):
  active_turtle.shape(active_gif)
  wn.update()

# this is a basic function that takes a turtle as a paramter, and moves it to the given x and y coordinates
def move(turtle, xx, yy):
    turtle.penup()
    turtle.goto(xx, yy)
    turtle.pendown()

# this is the function used to move the ball around    
def golf_hit():
    ball.penup()
    power_check = 0

    while power_check == 0: # this section will repeat until the numbers given by the user correctly allign with what is asked
        power_and_direction = input("How much power (1-10)?, What direction (0-359) (0 = East, 90 = North, 180 = West, 270 = South) - Format [Power:Direction] ")
        power_and_direction = power_and_direction.split(":")
        if int(power_and_direction[0]) < 11 and int(power_and_direction[0]) > 0:
            if int(power_and_direction[1]) < 360 and int(power_and_direction[1]) > -1:
                power_check = 1
    
    ball.seth(int(power_and_direction[1]))   
    ball.fd(int(power_and_direction[0])*40)

# creation of the countdown timer using the varaibles set at the beginning, the "counter" writes it by the top left
def countdown():
  global timer, timer_up
  counter.clear()
  counter.hideturtle()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# Creation of all the maps
def draw_map_one():
    pond_two.hideturtle()
    sand_three.hideturtle()
    sand_four.hideturtle()
    draw.color("#064C0D")

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

def draw_map_two():
   
    sand_three.hideturtle()
    sand_four.hideturtle()
    draw.color("#FFD300")

    move(ball, 250, 200)
    move(hole, -200, 200)
    move(pond_one, -85, 5)
    move(pond_two, -200, -200)
    move(sand_one, 130, 25)
    move(sand_two, 130, -100)
    move(draw, 350, 250)

    draw.seth(180)
    draw.fd(200)
    draw.penup()
    draw.fd(250)
    draw.pendown()
    draw.seth(270)
    draw.circle(125, 180)
    draw.seth(180)
    draw.penup()
    draw.fd(250)
    draw.pendown()
    draw.fd(200)

    draw.seth(270)
    draw.fd(500)
    draw.lt(90)
    draw.fd(650)
    draw.lt(90)
    draw.fd(500)
    draw.penup()

    draw.goto(20, 125)
    draw.pendown()
    draw.bk(200)
    

def draw_map_three():
    sand_three.hideturtle()
    sand_four.hideturtle()
    draw.color("#FF7800")

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

    draw.color("#E40010")

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

def choose_map():
    global which_map
    if which_map == "m_one":
        draw_map_one()
    if which_map == "m_two":
        draw_map_two()
    if which_map == "m_three":
        draw_map_three()
    if which_map == "m_four":
        draw_map_four()


# Assiagning each of the turtles to an image (for their shape) and creating the map all after the user inputs "ok"
if greeting == "ok":

    draw_turtle(ball, "golf_ball.gif")
    draw_turtle(sand_one, "sand.gif")
    draw_turtle(sand_two, "sand.gif")
    draw_turtle(sand_three, "sand.gif")
    draw_turtle(sand_four, "sand.gif")
    draw_turtle(pond_one, "pond.gif")
    draw_turtle(pond_two, "pond.gif")
    draw_turtle(hole, "hole.gif")

    choose_map()

    countdown()
    while timer_up == False:
        golf_hit()
        ball.onclick(return_home)

wn.mainloop() 