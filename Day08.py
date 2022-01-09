import turtle
ray = turtle.Turtle()
alan=turtle.Turtle()

def draw_triangle(t, side_length, color = "black"):
    """Drwas a triangle with rat the turtle.

    Parameters:
        side_length- the length of each side of the triangle
    """
    #like saying:
    #side_length =[value]
    #at the very start of the function
    # a variable exists...
    #Default parameter: you can supply a value that the parameter
    # will auromatically have if the user does not specify a different one. We will
    # not use them very much in class
    print("Side_Length:",side_length, "Color: ",color)
    t.color(color)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)


draw_triangle( ray,100, "green")

ray.penup()
ray.backward(200)
ray.pendown()
draw_triangle(alan,150, "red")
draw_triangle(ray,130, "black")
draw_triangle(alan,110, "blue")
draw_triangle(ray,90, "purple")
draw_triangle(alan,70, "yellow")
draw_triangle(ray,50, "pink")
    
    
