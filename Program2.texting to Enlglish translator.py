# Miguel de la Cruz Cabello
# COMS 103
# Program 2: texting to English translator
# 10/28/2019


# The purpose is to create a program that asks the user for some texting comunication and prints out an English translation.

def quit_function(): # Since the professor does not like 'break', I prefered to do the last function separated
    # and return it so the program would stop after passing to the last function and do the same job as 'break'.
    
    """ This function stops running the program.

    """
    
    print("Thank you for using this program")
    print("Good bye !!!")        

def main():
    print("Welcome to Miguel's texting to English translator.")
    print("Enter any line of text and it will be translated into English")
    print()
    texting_dictionary = {}# It is empty
    list_1 = [] # Stores the different translated lines
    with open("texting_to_english.txt") as f: # Opens the text file we are going to work with
        for line in f:
            line = line.strip()
            result = line.split("|")
            if len(result) == 2:
                key = result[0]
                value = result[1]
                texting_dictionary[key] = value
    while True:
        print("""Availabe options:
            (a) add a new texting to English translation
            (n) translate a new line
            (p) print all previous lines
            (q) to quit""")
        choice = input("Choose an option:")
        choice = choice.lower()

        if choice == "a": # This part of code adds a new line of text to the translator
            word = input("What is the new abbreviation you would like to translate? ")
            meaning = input("What does " + word + " mean in English"  "? ")
            print("Added " + word + " as " + meaning)
            print()
            texting_dictionary[word] = meaning

        elif choice == "n": # This code translates a line of texting to English
            text = input("Enter a line containing texting abbreviations to be translated: ")
            text = text.split()
            translation = ""
            for phrase in text:
                phrase = phrase.lower()
                if phrase in texting_dictionary.keys(): # Returns a view object that displays a list of all the keys in the dictionary
                    translation = translation + " " + texting_dictionary.get(phrase) # Returns the value for the specified key 
                else:
                    translation = translation + " " + phrase
            print( "Translated line:" + translation)
            print()
            list_1.append(translation) # Adds an item to the end of the list

        elif choice == "p":# This code prints all the stored translated lines
            print("Translated record:")
            for translation in list_1:
                print(translation)
                
        
        elif choice == "q": # This part of code finishes the program and gets out     
            return quit_function()
        
        else: # To prevent improperly data to enter in the system we use intput validation
            print("That is not a possible answer. Try again")
            print()
            

if __name__ == "__main__":
    main()
