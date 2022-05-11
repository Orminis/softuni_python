type_of_fuel = input()
liters_of_fuel = float(input())

if liters_of_fuel < 25:
    if type_of_fuel == "Diesel":
        print(f"Fill your tank with {type_of_fuel.lower()}!")
    elif type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
        print(f"Fill your tank with {type_of_fuel.lower()}!")
    else:
        print("Invalid fuel!")

else:
    if type_of_fuel == "Diesel":
        print(f"You have enough {type_of_fuel.lower()}.")
    elif type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
        print(f"You have enough {type_of_fuel.lower()}.")
    else:
        print("Invalid fuel!")