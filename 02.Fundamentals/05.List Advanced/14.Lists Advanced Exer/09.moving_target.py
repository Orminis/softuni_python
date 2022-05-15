########### Moving Target ##############
targets = [int(x) for x in input().split()]

command = input().split()

while command[0] != "End":

    action = command[0]
    index = int(command[1])
    number2 = int(command[2])

    if action == "Shoot":
        if 0 <= index <= len(targets):
            targets[index] -= number2         # Reducing the health of the target from the power of the shoot
            if targets[index] <= 0:           # Is the Target dead?
                targets.pop(index)

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, number2)      # Insert a new target on index with health = number2
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if (index + number2) <= len(targets) and (index - number2) >= 0:    #Check is the strike is going out of the length of the list
            del targets[index-number2:index+number2+1]                      #removing targets with slicing at once
        else:
            print("Strike missed!")

    command = input().split()

print("|".join(map(str, targets)))
