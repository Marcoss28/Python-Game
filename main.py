#import libraries & modules
import turtle
from turtle import * #Imports all of library's modules (import library first)
import random
from random import randint

#create a window
wn = turtle.Screen()
wn.bgcolor("#003b99") #You can type a color like "light blue" or go to "HTML color picker"

penup()
goto(-100, 180)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

speed(20)
penup()
goto(-200, 140)
color("white")

#define functions
def create_turtle(name , color):
  name.shape("turtle")
  name.color(color)

def track_name(name):
  write(name , True , align = "center" , font = ("Arial", 8, "normal"))

def turn(name , repeat , degrees):
  for turn in range(repeat):
    name.left(degrees)


def start(name , x , y):
  name.penup()
  name.goto(x , y)
  name.pendown()

# create a for loop that helps us draw the dashed track lines
for line in range(0 , 100 , 5):
  write(line + 5 , align = "center")
  right(90)

  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  
  penup()
  backward(160)
  left(90)
  forward(20)

x = -275
y = 100
goto(x , y)
track_name("Slowmalone")
goto(x , y - 25)
track_name("Tyrone")
goto(x , y - 50)
track_name("Jose")
goto(x , y - 75)
track_name("Karen")
goto(-100 , y - 150)

# Here we create a turtle
slowmalone = turtle.Turtle()
create_turtle(slowmalone , "green")

tyrone = turtle.Turtle()
create_turtle(tyrone , "black")

jose = turtle.Turtle()
create_turtle(jose , "A37E00")

karen = turtle.Turtle()
create_turtle(karen , "white")

# Let's send the turtle to the starting line
start(slowmalone , -222 , 100)
start(tyrone , -222 , 75)
start(jose , -222 , 50)
start(karen , -222 , 25)

# This for loop makes the turtle twirl
turn(slowmalone , 90 , 4)
turn(tyrone , 30 , 12)
turn(jose , 30 , 12)
turn(karen , 60 , 6)

# Create a for loop that makes our turtles race. Add your turtles to the race.
winner = ""
#for step in range(100):
while True:
  slowmalone.forward(randint(1 , 4))
  tyrone.forward(randint(2 , 6))
  jose.forward(randint(2 , 6))
  karen.forward(randint(1 , 5))
  if slowmalone.xcor() >= (180):
    winner = "Slowmalone"
    break
  elif tyrone.xcor() >= (180):
    winner = "Tyrone"
    break
  elif jose.pos() >= (180 , 50):
    winner = "Jose"
    break
  elif karen.pos() >= (180 , 25):
    winner = "Karen"
    break

print("The winner is " + winner + "!!!")
#State winner
w = "The winner  " + winner + "!!!"
track_name(w)
goto(225 , -50)