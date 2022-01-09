import turtle
ray = turtle.Turtle()
alan=turtle.Turtle()

def draw_triangle(t, side_length, color = "black"):
    """Draw a triangle with rat the turtle.

    Parameters:
        side_length- the length of each side of the triangle
    """
    #like saying:
    #side_length =[value]
    #at the very start of the function
    # a variable exists...
    #Default parameter: you can supply a value that the parameter
    # will automatically have if the user does not specify a different one. We will
    # not use them very much in class
    print("Side_Length:",side_length, "Color: ",color)
    t.color(color)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)

def main():
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
    
# When you turn in your program, essentially nothing should be on the very edge, EXCEPT certain orange keywords
# As a general rule, everything in yuor program that actually "does stuff", other than defined 
# In order to call the main function, we will include this block of code in almost every program
# if this is the main program, call the function 'main()' to start it up
if _name_ == "_main_":
    main()


def main():
    print("Welcome to the converters")
    print()

    while True:
        print("List of conversions")
        print("[inches] (to centimeters)")
        print("[centimeters] (to inches)")
        print()

        starting_unit = input("Enter the type of value you wish to convert")

        if starting_unit == "inches":
            result = inches_to_centimeters(value)
        elif starting_unit == "centimeters":
            result = centimeters_to_inches(value)

        #here is the last line of the while block
        # now everything jumps back to the top of this block

        print(result)
        print()
