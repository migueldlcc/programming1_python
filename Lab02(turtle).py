# Name: Miguel de la Cruz Cabello
# COMS 103
# LAB 02

# Create the turtle
import turtle
ben = turtle.Turtle()

# Type "Intro to program"
ben.width(7)
ben.penup()
ben.goto(-200,0)
ben.write("Introduction to Programming ", True, align="center",font=("Arial", 16, "normal"))

# Make the "B"
ben.width(4)
ben.penup()
ben.goto(-270,250)
ben.pendown()
ben.right(90)
ben.forward(163)
ben.left(90)
ben.forward(35)
ben.setheading(40)
ben.forward(37)
ben.setheading(90)
ben.forward(35)
ben.setheading(140)
ben.forward(37)
ben.setheading(180)
ben.forward(35)
ben.backward(35)
ben.setheading(40)
ben.forward(37)
ben.setheading(90)
ben.forward(35)
ben.setheading(140)
ben.forward(37)
ben.setheading(180)
ben.forward(35)

# Make the "L"
ben.color("red")
ben.width(4)
ben.penup()
ben.goto(-100,250)
ben.pendown()
ben.left(90)
ben.forward(163)
ben.left(90)
ben.forward(70)

# Make the "C"
ben.color("grey")
ben.width(4)
ben.penup()
ben.goto(90,250)
ben.pendown()
ben.setheading(180)
ben.circle(70,60)
ben.circle(100,70,70)
ben.circle(70,50)

#Make the star
ben.color("yellow")
ben.width(10)
ben.penup()
ben.goto(-20,7)
ben.pendown()
ben.setheading(250)
ben.forward(163)
ben.setheading(30)
ben.forward(170)
ben.setheading(180)
ben.forward(170)
ben.setheading(-30)
ben.forward(163)
ben.setheading(-247)
ben.forward(163)
