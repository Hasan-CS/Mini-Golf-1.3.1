# Made by Mohammed Jasim and Hasan Ahmad
# imports/basics
import turtle as trtl
import random as rand
wn = trtl.Screen()

### initialization
greeting = wn.textinput("Welcome to Golf Game!", '''Use the user inputs to move the ball and click the ball to reset it!
If you hit sand, then a hit is added to your score, and if you fall
in a pond the ball goes back to the starting point! Type 'ok' to begin: ''')

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
counter = trtl.Turtle()
score_writer = trtl.Turtle()

all_turtles = [draw, ball, sand_one, sand_two, sand_three, sand_four, pond_one, pond_two, hole, counter, score_writer]
for turtles in all_turtles:
    turtles.speed(0)

# All game images - this section also sets up background color, sizes and speed
wn.addshape("golf_ball.gif")
wn.addshape("pond.gif")
wn.addshape("sand.gif")
wn.addshape("hole.gif")

wn.bgcolor("#9BBC49")
wn.setup(800, 600)

draw.pensize(5)
ball.speed(2)

### variables and lists
# Different maps list + variable that stores a random map
map_list = ["m_one", "m_two", "m_three", "m_four"]
which_map = rand.choice(map_list)

# pre-setup (variables required for the timer and score to work)
font_setup = ("Arial", 20, "normal")
timer = 100
counter_interval = 1000   
timer_up = False
score = 0

# setting up the countdown and score turtle
counter.hideturtle(), score_writer.hideturtle()
counter.color("white"), score_writer.color("white")
counter.penup(), score_writer.penup()
counter.goto(-300, 255), score_writer.goto(-150, 255)

### fuctions
# this is the function used when the ball is clicked, it returns to the starting spot based on which map is chosen
def return_home(x, y):
    global which_map
    if which_map == "m_one":
        move(ball, -300, -200)
    if which_map == "m_two":
        move(ball, 250, 200)
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

# this is a basic function that updates the score
def update_score(): 
    global score
    score += 1
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)

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
    sand_check() # the sand check and pond check (later created) are both intregrated into the golf hit function, as well as update score
    pond_check()
    update_score() 
    

# this function checks if the ball is near sand, and tells it what to do if it is.
def sand_check():
    global which_map
    if which_map == "m_one" or "m_two" or "m_three":
        sand_list = [sand_one, sand_two]
    else:
        sand_list = [sand_one, sand_two, sand_three, sand_four]
    
    for turtles in sand_list:
        if ball.xcor() <= turtles.xcor() + 50 and ball.xcor() >= turtles.xcor() - 50:
            if ball.ycor() <= turtles.ycor() + 50 and ball.ycor() >= turtles.ycor() - 50:
                update_score()

# this function checks if the ball is near a pond, and tells it what to do if it is.
def pond_check():
    global which_map
    if which_map == "m_two" or "m_three" or "m_four":
        pond_list = [pond_one, pond_two]
    else:
        pond_list = [pond_one]
    
    for turtles in pond_list:
        if ball.xcor() <= turtles.xcor() + 50 and ball.xcor() >= turtles.xcor() - 50:
            if ball.ycor() <= turtles.ycor() + 50 and ball.ycor() >= turtles.ycor() - 50:

                if which_map == "m_one":   # this is just the "return home" function, but without the required parameters (the x and y coordinates of the click)
                    move(ball, -300, -200)
                if which_map == "m_two":
                    move(ball, 250, 200)
                if which_map == "m_three":
                     move(ball, 0, -200)
                if which_map == "m_four":
                    move(ball, 0, -100)

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
    
# creation of all the maps, note that we are drawing precise shapes and it is condensed as possible
def draw_map_one(): # start of map one (this map draws kind of a long, skinny rectangle that is connected to a tall, wide rectange - and there is a squarish piece taken off of top0left of the latter rectangle)
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

def draw_map_two(): # start of map two (this map draws a very wide rectangle with a semi-circle chipped off of it from the top - there is also a wall in the center reaching from the top down)
   
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
    draw.hideturtle()

def draw_map_three():  # start of map three (this map draws almost an upside-down boot - and there is a barrier reaching out from about where your ankle would be)
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
    draw.hideturtle()
    
def draw_map_four():  # start of map four (this map draws a large rectangle with two barriers reaching out from it - and an X in the center)

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

    draw.hideturtle()

# based on what "which map" is, the function selects to draw a random map out of four
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

### game
# assigning each of the turtles to an image (for their shape) and creating the map all after the user inputs "ok"
if greeting == "ok":

    draw_turtle(ball, "golf_ball.gif")
    draw_turtle(sand_one, "sand.gif")
    draw_turtle(sand_two, "sand.gif")
    draw_turtle(sand_three, "sand.gif")
    draw_turtle(sand_four, "sand.gif")
    draw_turtle(pond_one, "pond.gif")
    draw_turtle(pond_two, "pond.gif")
    draw_turtle(hole, "hole.gif")

    choose_map() # selecting the map
    countdown() # starting the timer, until the timer ends you can hit the ball and reset it

    while timer_up == False:
        golf_hit()
        ball.onclick(return_home)

        if ball.xcor() <= hole.xcor() + 30 and ball.xcor() >= hole.xcor() - 30:
            if ball.ycor() <= hole.ycor() + 30 and ball.ycor() >= hole.ycor() - 30:
                counter.penup(), counter.clear, counter.hideturtle()
                score_writer.clear()
                score_writer.write("You Win! Score: " + str(score), font=font_setup)
                timer = 0

wn.mainloop() 