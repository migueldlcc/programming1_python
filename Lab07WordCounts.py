# Miguel de la Cruz Cabello
# COMS 103
# Lab 07
# 10/16/2019

# Download accompanying file `book.txt`, place in same directory as this file.

# Three separate tasks:
# - count_letters()
#		Count the letters in the book
#		Print out the top 10 most used letters
# - count_words()
#		Count the words in the book
#		Print out the top 10 most used words
# - count_capitalized_words()
#		Count the capitalized words in the book
#		Print out the top 10 most used capitalized words

# We will work on the count_letters() function together in class
# and you will be responsible for the others.

# Each function should be called from main() and should print out
# its results, no returns necessary

def count_letters():
    """Count the total number of letters in the book file

    snd selects the 10 most used letters.

    """
    with open("book.txt") as f:
        # f.read() - will just pull in the entire file to a single string...
        # for line in f - you can deal with less text all at once, and
        # work just one line at a time....
        file_contents = f.read()

    total_letters = 0 # Accumulator
    letter_counts = {} # dictionary

    for character in file_contents:
        if character.isalpha():
            if character.lower() not in letter_counts:
                letter_counts[character.lower()] = 1
            else:
                letter_counts[character.lower()] += 1
            total_letters += 1
        
    print("Total letters:", total_letters)
    print()
    print(sorted(letter_counts, key=letter_counts.get, reverse=True)[:10]) # This means that we want to print the first 10 words


def count_words():
    """ This function counts the number of words in the file

    and selects the 10 most used words.
    

    """
    with open("book.txt") as f:
        file_contents = f.read()
        
    total_words = 0 
    word_counts = {}
    
    for word in file_contents.split():
        if word.isalpha():
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        total_words += 1

    print()   
    print("Total words:", total_words)
    print()
    print(sorted(word_counts, key = word_counts.get, reverse = True)[:10])

    
def count_capitalized_words():
    """ This function counts the capitalized words in the file

    and selects the 10 most used capitals.

    """
    import string # to put an atribute to "ascii_uppercase" we need to import the string 
    with open("book.txt") as f:
        file_contents = f.read()
    total_capitalized_words = 0
    cap_word_counts = {} # dictionary
    for capitalized_word in file_contents:
        if capitalized_word[0] in string.ascii_uppercase: # [0] means the very first character of the word, that it must be a capital letter
            if capitalized_word not in cap_word_counts:
                cap_word_counts[capitalized_word] = 1
            else:
                cap_word_counts[capitalized_word] += 1
        total_capitalized_words += 1
        
    print()
    print("Total capitalized words", total_capitalized_words)
    print()
    print(sorted(cap_word_counts, key = cap_word_counts.get, reverse = True)[:10])
    
            
def main():
    count_letters()
    count_words()
    count_capitalized_words()

if __name__ == "__main__":
    main()
