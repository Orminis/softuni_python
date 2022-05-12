age = float(input())
gender = input()

# Определяме пола
if gender == 'f':
    if age < 16:    #възраст
        print("Miss")
    else:
        print("Ms.")

elif gender == "m":
    if age < 16:    #възраст
        print("Master")
    else:
        print("Mr.")