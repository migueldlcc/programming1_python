# Name: Miguel de la Cruz Cabello
# COMS 103
# LAB O3

# 
def inches_to_centimeters():
    """This function coverts from inches to centimeters"""
    inches = int(input("How many inches?"))
    centimeters = inches * 2.54
    print(centimeters)

def centimeters_to_inches():
    """This function converts from centimeters to inches"""
    centimeters = int(input("How many centimeters?"))
    inches = centimeters * 0.39
    print(inches)

def liters_to_gallons():
    """This function converts from liters to gallons

    I looked the conversion factor on Internet
    """
    liters = int(input("How many liters?"))
    gallons = liters * 0.26
    print(gallons)
    
def gallons_to_liters():
    """This function converts from gallons to liters"""
    gallons = int(input("How many gallons?"))
    liters = gallons * 3.78
    print(liters)

def meters_to_yards():
    """This function converts from meters to yards

    I looed the conversion factor on Internet
    """
    meters = int(input("How many meters?"))
    yards = meters * 1.09
    print(yards)

def yards_to_meters():
    """This function converts from yards to meters"""
    yards = int(input("How many yards?"))
    meters = yards * 0.91
    print(meters)

def kilograms_to_pounds():
    """This function converts from kilograms to pounds

    I looed the conversion factor on Internet
    """
    kilograms = int(input("How many kilogrmas?"))
    pounds = kilograms * 2.20
    
    print(pounds)

def pounds_to_kilograms():
    """This function converts from pounds to kilograms"""
    pounds = int(input("How many pounds?"))
    kilograms = pounds * 0.45
    print(kilograms)

def fahrenheit_to_celsius():
    """This function converts from fahrenheit to celsius

    I looed the conversion factor on Internet
    """
    fahrenheit = int(input("How many fahrenheit?"))
    celsius = (fahrenheit - 32) *5/9
    print(celsius)

def celsius_to_fahrenheit():
    """This function converts from celsius to fahrenheit"""
    celsius = int(input("How many celsius?"))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

def demo():
    inches_to_centimeters()
    centimeters_to_inches()
    liters_to_gallons()
    gallons_to_liters()
    meters_to_yards()
    yards_to_meters()
    kilograms_to_pounds()
    pounds_to_kilograms()
    fahrenheit_to_celsius()
    celsius_to_fahrenheit()
