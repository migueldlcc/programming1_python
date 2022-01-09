# Miguel de la Cruz Cabello
# COMS 103
# 09/18/2019


# We define the main function
def main():
    print("Welcome to Miguel's converters program!")
    print()

    while True:
        print("List of conversions:")
        print("[inches] (to centimeters)")
        print("[centimeters] (to inches)")
        print("[liters] (to gallons)")
        print("[gallons] (to liters)")
        print("[meters] (to yards)")
        print("[yards] (to meters)")
        print("[kilograms] (to pounds)")
        print("[pounds] (to kilogram)")
        print("[fahrenheit] (to celsius)")
        print("[celsius] (to fahrenheit)")

        starting_unit = input("Enter the type of value you would like to convert: ")
        # Says what value you want to convert
        value = float(input("How many " + starting_unit + "? "))
        # Asks for the amount of units of that value you want to convert

        if starting_unit == "inches":
            result = inches_to_centimeters(value) 
        elif starting_unit == "centimeters":
            result = centimeters_to_inches(value)
        elif starting_unit == "litters":
            result = liters_to_gallons(value)
        elif starting_unit == "gallons":
            result = gallons_to_liters(value)
        elif starting_unit == "meters":
            result = meters_to_yards(value)
        elif starting_unit == "yards":
            result = yards_to_meters(value)
        elif starting_unit == "kilograms":
            result = kilograms_to_pounds(value)
        elif starting_unit == "pounds":
            result = pounds_to_kilograms(value)
        elif starting_unit == "fahrenheit":
            result = fahrenheit_to_celsius(value)
        elif starting_unit == "celsius":
            result = celsius_to_fahrenheit(value)
        print(result)
        print()
        
# Between the parenthesis of each function I put inches, centimeters, meters..
# as a signature
# Function inches to centimeters
def inches_to_centimeters(inches):
    """This function converts from inches to centimeters.
    Conversion factor: 1 in = 2.54 cm
    """
    centimeters = inches * 2.54
    return centimeters


# Function centimeters to inches
def centimeters_to_inches(centimeters):
    """This function converts from centimeters to inches.
    Cnversion factor: 1 in = 0.39 cm
    """
    inches = centimeters * 0.39
    return inches


# Function liters to gallons
def liters_to_gallons(liters):
    """This function converts from liters to gallons.
    Conversion factor: 1 L = 0.26 gallons
    """
    gallons = liters * 0.26
    return gallons


# Function gallons to liters
def gallons_to_liters(gallons):
    """This function converts from gallons to liters.
    Conversion factor: 1 gallon = 3.78 L
    """
    liters = gallons * 3.78
    return liters


# Function meters to yards
def meters_to_yards(meters):
    """This function converts from meters to yards.
    Parameters:
        meters - number of meters to convert.
    Conversion factor: 1 m = 1.09 yds
    """
    yards = meters * 1.09
    return yards


# Function yards to meters
def yards_to_meters(yards):
    """This function converts from yards to meters.
    Parameters:
        yards - number of yards to convert.
    Conversion factor: 1 yd = 0.91 m
    """
    meters = yards * 0.91
    return meters


# Function kilograms to pounds
def kilograms_to_pounds(kilograms):
    """This function converts from kilograms to pounds.
    Parameters:
        kilograms - number of kilograms to convert.
    Conversion factor: 1 kg = 2.20 lbs
    """
    pounds = kilograms * 2.20
    return pounds


# Function pounds to kilograms
def pounds_to_kilograms(pounds):
    """This function converts from pounds to kilograms.
    Paramters:
        pounds - number of pounds to convert.
    Conversion factor: 1 lb = 0.45 kg
    """
    kilograms = pounds * 0.45
    return kilograms


# Function fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    """This function converts from fahrenheit to celsius.
    Parameters:
        fahrenheit - number of degrees fahrenheit to convert.
    Conversion formula: celsius = (fahrenheit - 32) *5/9
    """
    celsius = (fahrenheit - 32) *5/9
    return celsius

# Function celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    """This function converts from celsius to fahrenheit.
    Parameters:
        celsius - number of degrees celsius to convert.
    Conversion formula: fahrenheit = (celsius * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



if __name__ == "__main__":
    main()


# I tried to put the units in the final result but I could not figure out how to do it



            


        

    
