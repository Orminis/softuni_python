"""
You are at the shooting gallery again, and you need a program that helps you keep track of moving targets.

On the first line, you will receive a sequence of targets with their integer values, split by a single space.
Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
    "Shoot {index} {power}"
        o Shoot the target at the index if it exists by reducing its value by the given power (integer value).
          A target is considered shot when its value reaches 0.
        o Remove the target if it is shot.
    "Add {index} {value}"
        o Insert a target with the received value at the received index if it exists. If not, print: "Invalid placement!"
    "Strike {index} {radius}"
        o Remove the target at the given index (if such exist) and the ones before and after it depending on the radius.
        o If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
            Example:  "Strike 2 2"
            	{radius}	{radius}	{strikeIndex}	{radius}	{radius}

    "End"
        o Print the sequence with targets in the following format:
         "{target1}|{target2} … |{targetn}"
"""

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
