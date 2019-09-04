import turtle
# Brings in the Turtle code
wn = turtle.Screen()
wn.bgcolor("orange")
# Creates the background
my_turtle = turtle.Turtle()
# Creates the turtle
my_turtle.color("purple")
my_turtle.penup()                #stops drawing
my_turtle.forward(-50)            #moves the turtle backwards
my_turtle.pendown()              #continues drawing
my_turtle.left(90)               #moves the turtle counterclockwise 90 degrees
my_turtle.forward(75)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.forward(-100)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(75)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.penup()
my_turtle.left(180)
my_turtle.forward(200)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.forward(75)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.forward(-100)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(75)
my_turtle.right(90)
my_turtle.forward(50)


tess = turtle.Turtle()
tess.shape("triangle")
tess.color("red")

tess.penup()
size = 20
for i in range(13):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.left(100)















wn.exitonclick()