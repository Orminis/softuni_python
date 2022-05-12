width = int(input())
length = int(input())
height = int(input())
free_box_space = width * length * height

operator = input()
needed_cubic = 0

while True:
    if operator == "Done":
        print(f"{free_box_space} Cubic meters left.")
        break
    else:
        operator_int = int(operator)
        free_box_space -= operator_int
        # if free_box_space < 0:
        #     print(f"No more free space! You need {abs(needed_cubic)} Cubic meters more.")
        #     break
        # elif free_box_space == 0:
        #     print(f"No more free space! You need {abs(needed_cubic)} Cubic meters more.")
        #     break
        # else:
        #     operator = input()
        #     if operator != "Done":
        #         operator_int = int(operator)
        #         needed_cubic = free_box_space - operator_int
        #     continue
        if free_box_space <= 0:
            print(f"No more free space! You need {abs(free_box_space)} Cubic meters more.")
            break
        else:
            operator = input()