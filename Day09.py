# Day09
# Create our own function that just does square root for us


#Let's say we wanted a function which just does this
def square_root(number):
    """Calculate the square root of a number

    Params:
        number - the number to take the square root of
    """
    result = math.sqrt(number)
    # Instead of printing the result, we need 
    # One exception to the rule that every function needs a docstring comment...no docstring comment is needed on the main function
def main():
    # Quadratic formula
    #
    # ax^2 + bx + c
    #
    # x = (-b (+/-) sqrt(b^2 - 4ac)) / 2a

    # We want to ask the user for a, b, and c
    # and then solve for x = 0 to see if it crosses the line

    # Ask the user for a, b, c (use input())
    float(input("Enter number a: "))
    float(input("Enter number b: "))
    float(input("Enter number c: "))

    # Run this calculation
    #  x = (-b (+/-) sqrt(b^2 - 4ac)) / 2a
    # two separate calculations:
    x_plus = (-b + square_root((b ** 2) - (4 * a * c))) / (2 * a)
    x_minus = (-b - square_root((b ** 2) - (4 * a * c))) / (2 * a)

    # Show the results to the user (use print())
    print(x_plus)
    print(x_minus)

    # What possibly could go wrong?
    # Divide by zero error
    # Check if a = 0. If it was zero, warn the user that this value will not work
    # = is the assigment operator....so this just assigns 0 to a
    # == is equality test
if a == 0:
    print("a must not be equal to zero! We cannot solve this, try again")
    # Don´t continue after this point...
    # return with nothing after it, inmediately ends the current function
    return
if (b ** 2) - (4 * a * c) < 0:
    print("There is no real slution with this input")
    return


  
    
