# Miguel de la Cruz Cabello
# COMS 103
# Program 3: Write a translator for English to Pig Latin
# 11/10/2019


# The purpose is to create a program that translates for English to Pig Latin

# Global Variables
VOWELS = "aeiouAEIOU"
CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
      
def translation(choice):
    """ This function translates a word in English to Pig Latin.

    """
    if choice[0] in CONSONANTS: # Words that start with a Consonant
        if choice.lower() == choice: # Words in lowercase
            choice = choice[1].lower()+ choice[2:].lower() + choice[0].lower()
            
        elif choice[0].upper() == choice[0] and choice[1:].lower() == choice[1:]:
            choice = choice[1].upper() + choice[2:] + choice[0].lower()

        elif choice[0].upper() == choice[0] and choice[1].lower() != choice[1:]:
            choice = choice[1].upper() + choice[2:] + choice[0].upper()    

        elif choice.upper() == choice:
            choice = choice[1:] + choice[0].upper()

##        elif choice[0].upper() == choice[0] and choice[1:].upper() == choice[1:]: # Words in uppercase
##            choice = choice[1:].upper() + choice[0].upper()
##                
##        elif choice[0].upper() == choice[0] and choice[1:].upper().lower() == choice[1:]: # Words starting in uppercase and with the rest of the letters in lowercase
##            choice = choice[1].upper() + choice[2:] + choice[0].lower()
##           
##        else: # Words with mixed upper and lowercase letters
##            choice = choice[1].upper() + choice[2:] + choice[0]
        return choice + "ay"

    elif choice[0] in VOWELS: # Words that start with a Vowel
        return choice + "way"
        
        

def main():
    print("Welcome to Miguel's Pig Latin translator!!!")
    print()
    while True:
        choice = input("Enter a word: ")
        result = translation(choice)
        if choice.upper() == choice: # To make the end of the word uppercase
            result = result.upper()
        print(result)
        
if __name__ == "__main__":
    main()            
