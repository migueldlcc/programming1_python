# Miguel de la Cruz Cabello
# COMS 103
# Program 4: Pig latin translator
# 12/04/2019
# I worked with Chris Quintero

import string # to put an atribute to PUNCTUATION we need to import the string
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
PUNCTUATION = string.punctuation #Includes, commas, periods, semicolons, whitespaces...

def punctuation(word):
    """ This function will help us to translate a line that include
    punctiations like ?./;:. """
    i = len(word)
    punctuation_1 = ""
    while word[0] in PUNCTUATION and i > 0:
        punctuation_1 += word[0]
        word = word[1:]
        i -= 1
        
    punctuation_2 = ""
    while word[-1] in PUNCTUATION and i > 0:
        punctuation_2 += word[-1]
        word = word[:-1]
        i -= 1
        
    result = translate_capitals(word)
    return punctuation_1 + result + punctuation_2

def hyphen(chunk): # Professor explained how to do this function in class
    """ This function translates words with hyphen. """
    chunks = chunk.split("-")

    for chunk in chunks:
        dictionary.append(punctuation(chunk))
        
    return "-".join(dictionary)

def translate_sentence(sentence):
    """ This function translates a full sentence. """
    dictionary = [] # list
    for word in sentence.split(): # Divides the sentence into words 
        dictionary.append(punctuation(word))
    return " ".join(dictionary)

def translate_consonant_word(word): # This part was given by the professor
    """ Translate one English word that starts with a consonant to Pig Latin."""
    if len(word) == 0 or word[0].lower() not in CONSONANTS:
        return word
    consonant_count = 0
    for letter in word:
        if letter.lower() in CONSONANTS:
            consonant_count += 1
        else:
            # As soon as we see a non-consonant, stop counting
            break
    result = word[consonant_count:] + word[:consonant_count] + "ay"
    return result
    

def translate_word(word): # This part was given by the professor
    """
    Translate one single word from English to Pig Latin, regardless of
    capitalization or other factors."""
    
    if len(word) == 0:
        return word
    
    # We act differently depending on if this is a consonant word or a vowel word
    if word[0].lower() in CONSONANTS:
        # This is fairly complex, so we'll use a function
        result = translate_consonant_word(word)
    elif word[0].lower() in VOWELS:
        result = word + "way"
    else:
        result = word
        
    return result

def translate_capitals(word): # This part was given by the professor
    """ Take an English word with no puncutation at the start or end and
    translate it into Pig Latin with the correct capitalization."""
    
    if len(word) == 0:
        return word
    
    has_all_capitals = word == word.upper()
    has_initial_capital = word[0] == word[0].upper()
    has_nonfirst_capital_and_lowercase_first_letter = len(word) > 1 and word[1:] != word[1:].lower() and word[0] == word[0].lower()

    result = translate_word(word)

    if has_all_capitals:
        result = result.upper()
    elif has_initial_capital:
        if len(result) > 1:
            result = result[0].upper() + result[1:]
        else:
            result = result[0].upper()
    elif has_nonfirst_capital_and_lowercase_first_letter:
        result = result[0].lower() + result[1:]

    return result


def main():
    print("Welcome to Miguel's Pig Latin Translator!!!")
    print()
    while True:
         print("""Availabe options:
            (a) Translate piglatin.txt file
            (b) Translate different sentences""")
         choice = input("Choose an option: ")
         choice = choice.lower()

         if choice == "a":
             with open("piglatin.txt") as f: # opens the 'txt' file
                 for sentence in f:
                     print(translate_sentence(sentence))

         elif choice == "b":
             sentence = input("Write the sentence you would like to translate: ")
             result = translate_sentence(sentence)
             print(result)
         else: # Input validation
             print("That is not a possible answer. Try again")
             print()

         answer = input("Would you like to run the program again?: ")
         answer = answer.lower()
         if answer == "yes" or answer == "y":
             continue # Keeps the program running

         elif answer == "no" or answer =="n":
             break # Stops the program

         else: # Input validation
             print("This answer is not valid!!!")
             print()

if __name__ == "__main__":
    main()
    

