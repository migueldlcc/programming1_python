# Program 4 second part
# Benoit Kabwar
# COMS 103
# I worked with Junior, Rebecca, Jean

import string

ALL_VOWELS = "aeiou"
ALL_CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALL_PUNCTUATION = string.punctuation

def translate_vowel_word(word):
    """Translate a single word which is known to start with a vowel.

    Parameters:
        word - the word to translate, must start with a vowel

    Returns the word with "way" appended.
    """
    result = word + "way"
    return result

def translate_line(line):
    """ This function helps us to translate a line in pig latin
    translator. """
    result = list()
    for word in line.split():
        re = word_with_hyphen(word)
        result.append(re)
    return ' '.join(result)

def word_with_punctuation(word):
    """ This function will help us to translate a line that include
    punctiations like ?./;:. """
    i = len(word)
    f_punctuation = ''
    while word[0] in ALL_PUNCTUATION and i > 0:
        f_punctuation += word[0]
        word = word[1:]
        i -= 1
        
    e_punctuation = ''
    i = len(word)
    while word[-1] in ALL_PUNCTUATION and i > 0:
        e_punctuation += word[-1]
        word = word[:-1]
        i -= 1
        
    result = translate_capitals(word)
    
    return f_punctuation + result + e_punctuation

def word_with_hyphen(word):
    """ This function will help us to translate words in pig latin
    translator that includ the hyphen. """
    result = list()
    words = word.split('-')
    
    for word in words:
        re = word_with_punctuation(word)
        result.append(re)
        
    return '-'.join(result)

def read_file():
    """ This function will help us to translate a file in pig latin translator.
    """
    name = input('Enter the name of the file: ')
    with open(name) as f:
        for line in f.readlines():
            
            print(translate_line(line))

def translate_consonant_word(word):
    """Translate a single word which is known to start with a consonant.

    Parameters:
        word - the word to translate, must start with a consonant

    Returns the word with all consonants moved to the end and "ay" appended.
    """
    i = len(word)
    while word[0].lower() in ALL_CONSONANTS and i > 0:
        word = word[1:] + word[0]
        i -= 1
    return word + "ay"

def translate_word(word):
    """Translate a single word from English to Pig Latin, ignoring capitalization.

    Parameters:
        word - the word to translate

    Returns the translated version of the word.
    """
    # Is this a vowel word or a consonant word?
    if word[0].lower() in ALL_CONSONANTS:
        result = translate_consonant_word(word)
    elif word[0].lower() in ALL_VOWELS:
        result = translate_vowel_word(word)
    return result

def translate_capitals(word):
    """Translate a single word from English to Pig Latin.

    Parameters:
        word - the word to translate

    Returns the resulting Pig Latin word
    """
    
    if len(word) < 1:
        return word

    # Detect what type of capitalization situation we have
    if word.lower() == word:
        is_mixed_case = False
        is_all_uppercase = False
        is_all_lowercase = True
    elif word.upper() == word:
        is_mixed_case = False
        is_all_uppercase = True
        is_all_lowercase = False
    else:
        is_mixed_case = True
        is_all_uppercase = False
        is_all_lowercase = False
        
    is_first_uppercase = word[0].upper() == word[0]
    only_first_uppercase = is_first_uppercase and len(word) > 1 and word[1:].lower() == word[1:]
    
    # Do some translating
    result = translate_word(word)


    # Handle the capitalization from before
    if is_all_lowercase:
        return result.lower()
    elif is_all_uppercase:
        return result.upper()
    elif is_mixed_case:
        if only_first_uppercase:
            return result[0].upper() + result[1:].lower()
        elif is_first_uppercase:
            return result[0].upper() + result[1:]
        else:
            return result

def main():
    while True:
        print("Welcome to the pig latin translator.")
        print()
        print('first - translate many lines')
        print()
        print('second - translate files')
        print()
        option = input('Select one of the options: ')
        print('')
        if option == 'first':
            line = input("Tape here to translate: ")
            result = translate_line(line)
            print(result)
        elif option == 'second':
            read_file() 
        

if __name__ == "__main__":
    main()
