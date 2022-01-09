# Miguel de la Cruz Cabello
# COMS 103
# 10/05/2019
# Program 1: rock, paper, scissors game


# Objective: Create a program that let us play 'rock', 'paper', 'scissors' against the computer.

def computer_choice():
    """ Creates a random choice for the computer either 'rock',

    'paper' or 'scissors'.

    """
    import random
    options = ['rock', 'paper', 'scissors']
    choice = random.choice(options)
    return choice


def human_choice():
    """ Gets the choice of the human and returns it either 'rock', 'paper'

    or 'scissors'.

    """
    while True:
        response = input("Enter 'rock', 'paper', or 'scissors':")
        if response.lower() == "rock" or response.lower() == 'r':
            return 'rock'
        elif response.lower() == "paper" or response.lower() == 'p':
            return 'paper'
        elif response.lower() == "scissors" or response.lower() == 's':
            return 'scissors'
        else:# input validation prevents improperly data to enter in the system
            print("Try again")  


def winner(computer_choice, human_choice):
    """ Determines the winner of the game.

    """
    
    if computer_choice == human_choice:
        return "Tie"
    elif computer_choice == "rock" and human_choice == "paper":
        return "Human"
    elif computer_choice == "paper" and human_choice == "scissors":
        return "Human"
    elif computer_choice == "scissors" and human_choice == "rock":
        return "Human"
    else:
        return "Computer"
        
def one_round_of_the_game():
    """ This function generates one round of the game.

    """
    resultComputer = computer_choice()
    resultHuman = human_choice()
    resultWinner = winner(resultComputer, resultHuman)

    print("Human chose", resultHuman)
    print("Computer chose", resultComputer)

    if resultWinner == "Human":
        print(resultWinner, "wins")
        print()
    elif resultWinner == "Computer":
        print(resultWinner, "wins")
        print()

    elif resultWinner == "Tie":
        print("Tie")
        print()
        
    return resultWinner


def main():
    """ This function runs the whole game and stores the final score until

    the user wants to leave the game.

    """
    
    print("Let us play Miguel's rock, paper, scissors program")
    print()
    print("You are playing against the computer")
    print()

    computerScore = 0
    humanScore = 0
    tieScore = 0

    while True:
        oneRound = one_round_of_the_game()
        print("Would you like to play again?")
        print()
        answer = input("Enter y for yes or n for no: ")

        if oneRound == "Computer":
            computerScore += 1
        elif oneRound == "Human":
            humanScore += 1
        elif oneRound == "Tie":
            tieScore += 1

        if answer == 'y' or answer == "yes":
            continue
        elif answer == 'n' or answer == "no":
            break
        else:
            print("That is not a possible answer")
        # I found the use of continue and break in a video I watched and then I
        # searched the definitions in the link for Python Documentation that is
        # posted in myblc

            
    print("Thanks for playing!!!")
    print()
    print("Final result:")
    print("Computer wins", str(computerScore), "times") # Converts whatever it
    # passes in to a string
    print("Human wins", str(humanScore), "times")
    print(str(tieScore), "ties")
    print()
    print("Goodbye")


if __name__ == "__main__":
    main()
    
        
        
        

