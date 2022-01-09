

# Constant file name:
#FILE_NAME = "numbers.txt"

# Our programs use human input to produce results interactively

# Sometimes we want to do a lot of things without having to
# type each one in by hand


# We can try to make a program that will work for an entire
# batch of input all at once...


# Let's start with a basic version that works the way we know.

# "Calculate the average of a series of numbers"
def calculate_average():
    total = 0
    count = 0

    value = int(input("Enter the next number, -1 to quit: "))
    while value != -1:
        total += value
        count += 1

        value = int(input("Enter the next number, -1 to quit: "))

    average = total / count
    print("The average is", average)


# We want this to work for 100s of numbers without
# needing to type them in again....

# We want to be able to open and read from a text file
# with Python and accomplish the same result.

def file_average():
    """Calculate the average of some numbers that are
    in a text file, one per line.
    """

    # How can we open a text file?

    # Open looks for a specific file on your system
    # If it is just the file name, it will look
    # in the same directory.
    # If it is an entire path C:\...\..\...
    # That will also work

    file_name = input("Enter file name: ")
    #file_name = "numbers.txt"
    # 'f' is a reference to the opened file
    # that lets us interact with it
    total = 0
    count = 0
    with open(file_name) as f:
        # Stuff goes inside

        # One way to interact with a file
        # is to loop over it one line at a time:
        for line in f:
            # When you loop over a file one line
            # at a time, that 'line' includes the
            # newline character at the end of
            # each line

            # Typically when we use 'for line in f'
            # we will "strip off" the newline character
            # from the end of the line immediately:
            line = line.strip() # removes leading and trailing white space

            # Any time we work with file input, each line is a STRING
            # if you want a number, you have to convert it:
            value = int(line)
            # You will almost always call strip() on the line...
            #print(line)
            total += value
            count += 1

    average = total / count
    print("The average is", average)    

def process_words():
    with open("words.txt") as f:
        # file.read() reads in the entire file as a string
        #contents = f.read()

##        # if you specifcy a parameter, it reads that many bytes:
##        contents = f.read(5)
##        print(contents)
##        contents = f.read(5)
##        print(contents)

        # file.readlines() reads the file lines into a list of strings
        contents = f.readlines()
        print(contents)

##        # file.readline() reads one line of the file at a time
##        contents = f.readline().strip()
##        print(contents)
##        contents = f.readline().strip()
##        print(contents)
        


def main():
    process_words()
    #file_average()
    #calculate_average()

if __name__ == "__main__":
    main()
