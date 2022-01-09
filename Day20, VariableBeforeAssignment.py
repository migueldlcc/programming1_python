


# New lab Wednesday (1 week)
# New program Friday (2 weeks)


# Program 1 due Wednesday

# Common error: Variable referenced before assignment

### Have a nice variable:
##choice = "rock"
##
### We do something with it other than assignment:
##if choice == "rock":
##    print("You win!")

# If these are out of order, then we would have a reference before assignment:

##if choice == "rock":
##    print("You win!")
##
##choice = "rock"


# Sometimes we attempt to assign a variable and for some reason we just don't get it quite right:
choice = input("Enter something:")

# Set a default value before you start (only if it makes sense):
result = "...something..."

if choice == "rock":
    result = 'r'
elif choice == "scissors":
    result = 's'
elif choice == "paper":
    result = 'p'
else:
    # What to do if none of the above

# At this point in the program, there is **no guarantee**
# that the variable `result` will exist at all:
if result == "rock": # This could very likely have an error for the variable not being assigned yet
    print("You win!")

# Another way:
for i in range(n):
    result = 5

    # If this loop never runs once, then result will never be set

# Possible helps:

# 1. If you're assigning a variable inside multiple if statements, use elifs **and** an else at the end

# 2. Assign the variable a default value before the if statements if that makes sense









