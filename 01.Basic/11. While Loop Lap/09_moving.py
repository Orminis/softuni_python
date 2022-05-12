wide_of_free_space = int(input())       # Размери на свободното пространство
lenght_of_free_space = int(input())
hight_of_free_space = int(input())


free_space = wide_of_free_space * lenght_of_free_space * hight_of_free_space  # Големина на свободното място
occupied_space = 0                # Променлива в която събираме кашоните
boxes = input()              # брой кашони (всеки кашон е 1куб м)

while boxes != "Done":
    new_space = int(boxes)
    occupied_space += new_space         # Добавяме кашоните към заетото място

    if occupied_space > free_space:    # Ако заетото място е повече от свободното прекъсваме програмата
        needed_space = occupied_space - free_space
        print(f"No more free space! You need {needed_space} Cubic meters more.")
        break

    boxes = input()

else:                               # Ако ни е останало свободно място
    left_space = free_space - occupied_space
    print(f"{left_space} Cubic meters left.")
