# Miguel de la Cruz Cabello
# COMS 103
# Lab09
# 12/05/2019


## Task 1
## Create a kaleidoscope from an image
## Slice into 8 pieces, copy one of them
## to cover all 8 regions

import cImage
fileName = "simpsons.gif"
windowName = "Kaleidoscope"

""" A kaleidoscope is a tube containing mirrors and pieces of colored paper
whose refections produce changing patterns."""

image = cImage.FileImage(fileName)
height = image.getHeight()
width = image.getWidth()

window = cImage.ImageWin(windowName, width, height)
image.draw(window)
print("Image height:", height, "Image width:", width) 

for row in range(height // 2):
    for col in range(row):
        pixel = image.getPixel(col, row)
        image.setPixel(row, col, pixel)
        image.setPixel(222 - row, col, pixel)
        image.setPixel(col, 222 - row, pixel)
        image.setPixel(222 - col, row, pixel)
        image.setPixel(222 - row, 222 - col, pixel)
        image.setPixel(222 - col, 222 - row, pixel)
        image.setPixel(row, 222 - col, pixel)
        # I had some trouble with the Kaleidoscope because it did not close all the image and you can see some thin lines on the image.
        # I tried to make the dimensions bigger and smaller and this is the closest I came   


## Task 2
## Simplify an image to use fewer total colors
## Apply posterization to make the image use
## only 8 colors. The starting code below
## gets most of the extra work out of the way
## so you can focus on the colors.

fileName = "simpsons.gif"
windowName = "Posterization"

""" Posterization is the process to create posters """

image = cImage.FileImage(fileName)
height = image.getHeight()
width = image.getWidth()
window = cImage.ImageWin(windowName, width, height)
image.draw(window)
for row in range(image.getHeight()):
    for col in range(image.getWidth()):
        pixel = image.getPixel(col, row)
        red = pixel.getRed()
        blue = pixel.getBlue()
        green = pixel.getGreen()
        
        # If red >> blue, green, make the pixel red!

        if red <= 100: #Purple
            pixel.setRed(130)
            pixel.setBlue(210)
            pixel.setGreen(0)

        elif blue >= 190: # Orange
            pixel.setRed(210)
            pixel.setBlue(0)
            pixel.setGreen(130)

        elif green <= 50: # Black
            pixel.setRed(0)
            pixel.setBlue(0)
            pixel.setGreen(0)

        elif green >= blue and green >= red: # Yellow
            pixel.setRed(240)
            pixel.setBlue(0)
            pixel.setGreen(240)

        elif blue <= 12: #Pink
            pixel.setRed(210)
            pixel.setBlue(130)
            pixel.setGreen(150)
            
        elif green <= red and green <= blue: # Green
            pixel.setRed(0)
            pixel.setBlue(0)
            pixel.setGreen(155)

        elif red >= green and red >= blue: # Red 
            pixel.setRed(155)
            pixel.setBlue(0)
            pixel.setGreen(0)

        elif blue >= red and blue >= green: # Blue
            pixel.setRed(0)
            pixel.setBlue(155)
            pixel.setGreen(0)

        else: # I did this to paint all the empty pixels so I don't get more than 8 colors.
            pixel.setRed(0)
            pixel.setBlue(0)
            pixel.setGreen(0)
            
        image.setPixel(col, row, pixel)


# Task 3
# Shrink an image down by a factor of 1/2

windowName = "Blank"
fileName = "simpsons.gif"

image = cImage.FileImage(fileName)
height = image.getHeight()
width = image.getWidth()

newImage = cImage.EmptyImage(height // 2, width // 2)
width = (width// 2) # Coordinate to make the width half smaller
height = (height// 2) # Coordinate to make the height half smaller
window = cImage.ImageWin(windowName, width, height)

for col in range(width):
    for row in range(height):
        pixel = image.getPixel(row * 2, col * 2)# You write pixel otherwise you will get a NameError
        newImage.setPixel(row, col, pixel)
              
newImage.draw(window)
print("Image height:", height, "Image width:", width)






