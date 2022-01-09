# Lab 6

# Try to run this file. It should draw a scene. Your job is to make some
# corrections to the scene.  This turtle was called Speedy.

# 1. Speedy is really slow, make him go faster so it doesn't take so long. /
# 2. There is a stray line from the corner of the house up to the roof,
#    make it go away. /
# 3. Put a purple door on the house. /
# 4. The grass is really long. Cut it by making it shorter.
# 5. Make it sunset -- the sun should be halfway below the horizon and
#    the sky should be darker. If you draw it first, then you can cover
#    it up with other stuff later.
# 6. Put your name in the picture after the name of the college. /

# Feel free to make any other artistic changes if you wish.

# When you are done, take a screenshot of the result to turn in along
# with the updated code file.


import turtle


def drawScene():
    speedy = turtle.Turtle() ## construct a turtle to use
    speedy.penup()  ## draw later
    speedy.speed(2) ## choose how fast to run speedy, 10 is fast, 0 is fastest

    ## lower portion of screen is ground -- a brown rectangle
    speedy.goto(-400, -300)     ##  go to lower left corner of window.
    speedy.color('brown')
    speedy.begin_fill()
    for i in range (2): ##  draw a rectangle --
        speedy.speed(0)
        speedy.forward(800)     ##  long side
        speedy.left(90)
        speedy.forward(200)     ##  short side
        speedy.left(90)
    speedy.end_fill()

    ## upper portion of screen is sky -- a blue rectangle
    speedy.goto(-400, -100)     ##  go to lower left corner of sky.
    speedy.color('dark blue')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(800)
        speedy.left(90)
        speedy.forward(400)
        speedy.left(90)
    speedy.end_fill()
    
    ## lower part of house -- a salmon-colored rectangle
    speedy.goto(0, -100)     ##  go to lower left corner of window.
    speedy.color('salmon')
    speedy.begin_fill()
    for i in range (2):         ##  draw a rectangle
        speedy.forward(300)
        speedy.left(90)
        speedy.forward(160)
        speedy.left(90)
    speedy.end_fill()

    ##  the roof
    speedy.penup()
    speedy.color('tan')
    for x in range(-30, 330, 4):    ##  draw a sequence of line segments
        speedy.goto(150, 150)       ##  peak of roof
        speedy.goto(x, 60)          ##  point along drip edge
        speedy.pendown()
    speedy.penup()

    ##  the door
    speedy.goto (130, -100)
    speedy.color('purple')
    speedy.begin_fill()
    for i in range(2):
        speedy.forward(60)
        speedy.left(90)
        speedy.forward(100)
        speedy.left(90)
    speedy.end_fill()


    ##  grass

    speedy.goto(-400, -100)         ##  left end, where ground meets sky
    speedy.color('green')   
    for x in range(-400, 400, 6):   ##  iterate through blades
        speedy.left(85)             ##  leans slightly
        speedy.pendown()
        speedy.forward(15)          ##  draw blade
        speedy.penup()
        speedy.right(180)           ##  turn around
        speedy.forward(15)          ##  traced over it again
        speedy.left(95)
        speedy.forward(6)
    speedy.penup()

    ##  sun in the sky

    speedy.goto(-200, 50)
    speedy.pendown()
    speedy.color('gold', 'yellow')
    speedy.begin_fill()
    for i in range(18):
        speedy.forward(40)
        speedy.right(170)
    speedy.end_fill()
    speedy.penup()

    ##  add a greeting
    speedy.goto(-300, -200)
    speedy.pendown()
    speedy.write("Bethany Lutheran College     ", align='center', font=('Arial', 12, 'normal'))
    speedy.penup()
    speedy.goto(-300,-250)
    speedy.pendown()
    speedy.write("Miguel de la Cruz Cabello", align = 'center', font = ('Arial', 12, 'normal'))

if __name__ == "__main__":
    drawScene()

