# General rule: assume the user of your program doesn't make any mistakes....
#unless the assignment specifically asks for something special

#control flow: making your program do something other than just running
#every statement in order from top to botton

# if
# an elif is a way to extend an if statement
# to cover more than just one situation.
# elif can only come after an if, and is going
# to be tied to the one above it.

# There is one more option with these called 'else'
# any time you get to the 'else', that block
# will always be executed and there is not a
# boolean condition

number = int(input("Enter a number: "))
if number > 4:
    print("The number was fairly large!")
    # only execute if the statement was true

elif number <= 3:
    print("This is not a big number")
elif number == 6:
    print("You win")
if number > 10:
    print("The number was huge!")
elif number < 0:
    print("The number is tiny")
else:
    print("That number is not very interesting")

#loop
number = int(input("enter a number"))

# while keyword starts a loop...
# anything inside the block following while
# will happen over and over again until
# the condition becomes false

print("before loop")
while number <= 100:
    # the test happens before the contests are executed
    print(number)
    number = number + 1
print("after loop")

answer = input("Enter a nice word: ")
while answer != "quit" and answer != "coms103":
    #!= is not equal
    print(answer)
    answer = input("Enter a nice word: ")
