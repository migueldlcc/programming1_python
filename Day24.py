
for word in words:
    if word[0] in string.ascii_uppercase:
        count += 1


my_string = "This is a really great string"
# [x] takes the xth letter of the string or the xth item of a list
# "the index operator"
# counts starts at 0 and goes up to 1 less than the
# [-x] counts from the back of the string...
# (the last letter is -1)
# frecuently we onle need to see the very end, unless 
print(my_string[2]) #take the 3rd letter of the string


print(my_string[-1])
print(my_string[-2])
print(my_string[-10])

# slicers

# Take the normal index operator, but instead of just one number, supply two:
# the start and the end

print(my_string[2:14])

# [x:y] means starts at index, go through one less than y

# This matches the same patterns we see on the range() function, where we start
# at 0 or the first parameter and stop one less than the second parameter

print(my_string[17:22])

#Frecuently we will be following a pattern or carefully calculating these numbers
# to create a slice

# If you want to go all the way to the start or end of the string on one side of
# the slice, just leave that number blank:

# Skip the first 3 characters:
print(my_string[3:])

# Skip the last 2 characters:
print(my_string[:-2])


# There is the option of supplying a third number to your list slicer:

# [start: stop:end]
# *Just* like the range function
# not as useful with strings, often with list


