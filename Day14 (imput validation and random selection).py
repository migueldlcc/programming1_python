

def computer_choice():
    """Generates a random choice for the computer either

    'rock', 'paper', 'scissors'
    """
    options = ['rock', 'paper', 'scissors']
    choice = random.choice(options)
    return choice
    # We don't print from our smaller functions, intead we return
    # values that can be both printed and examined later....
def main():
    #Testing out return walues....
    # A parameter lets you pass data IN to a function
    # A return value lets you pass data OUT of a function
    # Any time you call a funtion that returns your data,
    # you probably want to campture the result in a variable
    result = computer_choice()


def human_choice():
    while True: # loop forever...only way out is to return
        #Ask the user for some input, return either rock, paper, scissors
        response = input( "Enter 'rock', 'paper', or 'scissors':")

        #Make sure they chose either 'rock', 'paper', or 'scissors'

        if response.lower() == "rock":
            return 'rock'
        elif response.lower() == "paper":
            return 'paper'
        elif response.lower() == "scissors":
            return 'scissors'
        # Print anerror message to let the user know they messed up
        else:
            print("That is not an accepted answer. Try again")

def main():
    result = human_choice()
    print(result)

if __name__() == "__main__":
    main()


