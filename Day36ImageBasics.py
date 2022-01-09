windowName = "My Window"
fileName = "waldo_medium.gif"

# Using cImage requires cImage.py
# file in the same directory
import cImage

# FileImage is like opening up a text file,
# but for images instead
image = cImage.FileImage(fileName)

# Get the height and width from the image
height = image.getHeight()
width = image.getWidth()
print("Image height:", height, "Image width:", width)

# Create a window to put the image in
window = cImage.ImageWin(windowName, 3 * width, height)

# Draw the image into a window
image.draw(window)

# We're discovering the "API" of the cImage module.
# That stands for Application Programming Interface
# The list of methods that we can interact with
# the cImage library using.

# Make a copy of the image for manipulation
imageCopy = image.copy()

# Save a copy of the image as it is
imageCopy.save("waldo_copy.gif")

# Loop over the image across each row
# from the top left, then down one column
# at a time until the bottom right
for row in range(image.getHeight()):
    for col in range(image.getWidth()):
        # Do *something*

        # Get the value of this pixel
        pixel = image.getPixel(col, row)

        # These pixels use RGB color,
        # where a pixel consists of 3 integer
        # values between 0 and 255. One for
        # each of Red, Green, and Blue

        # Get one specific color value,
        # a number from 0 to 255
        red = pixel.getRed()
        blue = pixel.getBlue()
        green = pixel.getGreen()

        # Modify the color of the pixel
        pixel.setRed(255 - red)
        pixel.setBlue(255 - blue)
        pixel.setGreen(255 - green)


        # Calculate the average color value
        # for this pixel
        average = (red + green + blue) // 3

        if average > 150:
            pixel.setRed(255)
            pixel.setBlue(255)
            pixel.setGreen(255)
        else:
            pixel.setRed(0)
            pixel.setBlue(0)
            pixel.setGreen(0)            

        # Modify the original image with
        # this new pixel
        image.setPixel(col, row, pixel)

    image.draw(window)


