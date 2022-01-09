# The classroom microphone is missing
# so for now there is no audio....

# I will just type everything important into a
# file somewhere...


# (Any questions on Lab 04)


# We will do a new Lab 05 on Friday, so don't get behind

# Today's goal is to use some of the new tools
# we learned in the last few class periods

# We will expand on a previous turtle program to
# add new functionality that we couldn't accomplish before



import turtle

def draw_polygon(t, sides, side_length, color="black"):
    """Draws a polygon with the turtle.

    Parameters:
        t - the turtle
        sides - the number of sides in the shape
        side_length - the length of each side of the square
        color - the color of the square
    """
    angle = 360 / sides
    
    t.color(color)
    
    for i in range(sides):
        t.forward(side_length)
        t.left(angle)

def main():
    joe = turtle.Turtle()

    # A 3 sided polygon is a triangle
    draw_polygon(joe, 3, 150, "purple")

    # We got 3 sides but the angle was wrong....

    # Let's make sure we understand what's going on.

    steve = turtle.Turtle()
    steve.penup()
    steve.goto(-100, -100)
    steve.pendown()

    draw_polygon(steve, 4, 100, "red")

    joe.penup()
    joe.goto(-150, 100)
    joe.pendown()
    draw_polygon(joe, 6, 75, "blue")
    
    draw_polygon(joe, 11, 75, "black")

    draw_polygon(steve, 5, 50, "green")
    
# Notice that the final function is shorter than the original one
# but also does more.....we combined repeated behavior and simplified
# the overall program---this is very common in programming and almost
# always desirable

##def draw_polygon(t, sides, side_length, color="black"):
##    """Draws a polygon with the turtle.
##
##    We need to know the number of sides requested,
##    and ALSO we need to translate that number of sides
##    into an angle with some kind of formula.
##
##    Parameters:
##        t - the turtle
##        sides - the number of sides in the shape
##        side_length - the length of each side of the square
##        color - the color of the square
##    """
##
##    # We know the number of sides....how can we turn that
##    # into an angle for each turn
##
##    # A square has 4 sides of 90 degrees --> 360 / 4 = 90
##    # A triangle has 3 sides of 120 degrees --> 360 / 3 = 120
##    # A pentagon has 5 sides of 72 degrees --> 360 / 5 = 72
##    # A hexagon has 6 sides of ... 360 / 6 = 60 degrees
##    # etc. etc.
##
##    # The interior angle of our shape should add up to
##    # the same amount in all these cases because we start
##    # and finish with the turtle facing the same direction
##
##    # A full circle is 360 degrees, so we will break that up
##    # into N number of turns by dividing 360 by the number of sides
##    
##    # What all do we need to change so this draws a SQUARE?
##
##    # 1. Change the turning angle....90 degrees for a square
##    # 2. Draw one additional line after turning
##
##
##    angle = 360 / sides # use this angle instead of the hard-coded 90
##
##    # We need to use the number of sides to control how many
##    # times we do the forward and left lines
##    t.color(color)
##
##    # We will use the loop to run the same code multiple times
##    # it will be important to control exactly how many times
##    # that loop runs
##
##    # There is a new type of loop that is made to make this
##    # very common situation easier to deal with
##
##    # In this new type of loop, the keyword is 'for':
##    # In a for loop, the variable 'i' represents how many times
##    # you have gone through the loop
##
##    # for i in range(sides) means "run the following code the number
##    # of times that the variable sides is"
##
##    # If sides == 5, this will run 5 times, etc.
##    for i in range(sides):
##        # These two lines are the ones that keep happening
##        # over and over again, so we want them to run
##        # one time for each side of the shape
##        t.forward(side_length)
##        t.left(angle)
##
##        # There are no longer any numbers in this important part
##        # of the code...it's all just depending on the variables
##
##        # This section of code ran 3 times because we filled
##        # in 3 for the parameter 'sides'
##
##        # We need to fix the angle
##
##        # This isn't done yet but let's test it out.
    
# Goal: Update the draw_triangle function
# so it will draw a shape of a given
# number of sides....square, pentagon, etc.

# We want 1 function that can do all of those
# different shapes depending on the parameter chosen

# Let's create a draw_square() function just to see
# how a square differs from drawing a pentagon


# Now we have 2 separate functions, let's compare them
# to see if there are similarities and what parts specifically
# are different...

# We want to take the similar parts and reuse those,
# then use parameters and/or variables to control
# the parts that are different so we can draw multiple
# shapes with one function




if __name__ == "__main__":
    main()
