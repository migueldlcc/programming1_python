

# Load the text file into a dictionary

texting_dictionary = {}

# Dictionary has a key -> value relation

# What are the keys and what are the values?

# The key is the thing you know, and you wish to look up...

# Keys: texting word
# Values: english word
with open("texting-in-english.txt") as f:
    for line in f:
        line = line.strip()
        # we have something of the form: key|value
        # we need to split it apart
        # so we can access each portion individually
        result = line.split("|")
        key = result[0]
        value = result[1]
        texting_dictionary[key] = value
        print(texting_dictionary)
        print(texting_dictionary["ur"])

# How in the world do I store my data???
 
