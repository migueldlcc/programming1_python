# Miguel de la Cruz Cabello
# COMS 103
# 09/27/2019
# LAB 05


# Part 1

def factorial(n):
    """
    Calculate the factorial of a number

    Parameters:
    n - The number to take the factorial of

    Prints the factorial of n, no return
    """
    acc = 1 # we want to start from 1 and up
    for i in range(1, n):
        # The range starts with 1 and ends with n.
        # Example: n = 5, range(1,5) which is the same as [1,2,3,4,5]
        acc = acc * (i+1)
        # Instead of adding each number of the list, we multiply them     
    print( "The factorial is", acc)


# Part 2

def fibonacci():
    """ This function finds a fibonacci number
    Parameters:
        n - number to find in the fibonacci formula
    """
    n = int(input("Select a number: ")) #Defined variable name
    fib_0 = 0
    fib_1 = 1
    fib_n_minus_2 = fib_0
    fib_n_minus_1 = fib_1
    if n == 0:
        print(fib_0)
    elif n == 1:
        print(fib_1)
    else:
        for i in range(2, n + 1):
            fib_n = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
        print("The number in the fibonacci list is", fib_n)

def main():
    factorial()
    fibonacci()

if __name__ == "__main__":
    main()

    

