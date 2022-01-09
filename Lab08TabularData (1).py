# Miguel De la Cruz Cabello
# COMS 103
# Lab 09

# Create a list to hold information about 10 cars
# Each entry in the list will have the following properties
#   Make
#   Model
#   Color (string with full color, e.g. "Blue")
#   Price (integer only)
#   Sale Discount (if any) (integer only)

def main():
    print("{:12}|{:12}|{:12}|{:12}|{:12}|{:12}".format("Make", "Model","Color", "Price", "Discount", "Total price"))
    print("{:-<12}|{:-<12}|{:-<12}|{:-<12}|{:->12}|{:-<12}".format("","","","","",""))
    cars = []

    car_1 = {}
    car_1['make'] = "Buick"
    car_1['model'] = "Roadmaster"
    car_1['color'] = "BLU"
    car_1['price'] = 1000000
    car_1['discount'] = 50000
    car_1['total price'] = car_1['price']- car_1['discount']

    cars.append(car_1)

    car_2 = {}
    car_2['make'] = "Audi"
    car_2['model'] = "R8"
    car_2['color'] = "BLA"
    car_2['price'] = 1240000
    car_2['discount'] = 12000
    car_2['total price'] = car_2['price']- car_2['discount']

    cars.append(car_2)

    car_3 = {}
    car_3['make'] = "Mercedes"
    car_3['model'] = "Benz SLS"
    car_3['color'] = "SIL"
    car_3['price'] = 1859400
    car_3['discount'] = 442600
    car_3['total price'] = car_3['price']- car_3['discount']

    cars.append(car_3)

    car_4 = {}
    car_4['make'] = "Peogeot"
    car_4['model'] = "2008"
    car_4['color'] = "GRE"
    car_4['price'] = 2199000
    car_4['discount'] = 476000
    car_4['total price'] = car_4['price']- car_4['discount']

    cars.append(car_4)

    car_5 = {}
    car_5['make'] = "BMW"
    car_5['model'] = "X3X"
    car_5['color'] = "WHI"
    car_5['price'] = 647900
    car_5['discount'] = 17900
    car_5['total price'] = car_5['price']- car_5['discount']

    cars.append(car_5)


    car_6 = {}
    car_6['make'] = "Seat"
    car_6['model'] = "Leon"
    car_6['color'] = "RED"
    car_6['price'] = 799000
    car_6['discount'] = 63200
    car_6['total price'] = car_6['price']- car_6['discount']

    cars.append(car_6)

    car_7 = {}
    car_7['make'] = "Volvo"
    car_7['model'] = "V40"
    car_7['color'] = "PIN"
    car_7['price'] = 2090000
    car_7['discount'] = 200000
    car_7['total price'] = car_7['price']- car_7['discount']

    cars.append(car_7)

    car_8 = {}
    car_8['make'] = "Chevrolet"
    car_8['model'] = "Camaro"
    car_8['color'] = "YEL"
    car_8['price'] = 4590000
    car_8['discount'] = 320000
    car_8['total price'] = car_8['price']- car_8['discount']

    cars.append(car_8)

    car_9 = {}
    car_9['make'] = "Honda"
    car_9['model'] = "Jazz"
    car_9['color'] = "MAG"
    car_9['price'] = 4470000
    car_9['discount'] = 509000
    car_9['total price'] = car_9['price']- car_9['discount']

    cars.append(car_9)


    car_10 = {}
    car_10['make'] = "Opel"
    car_10['model'] = "Corsa"
    car_10['color'] = "PUR"
    car_10['price'] = 3360000
    car_10['discount'] = 1640000
    car_10['total price'] = car_10['price']- car_10['discount']

    cars.append(car_10)

    for car in cars:
        print("{:12}|{:12}|{:12}|${:11,.2f}|{:12,.2f}|${:12}".format(car['make'], car['model'], car['color'], car['price']/100, car['discount']/100, car['total price']/100))

if __name__ == "__main__":
    main()
 

