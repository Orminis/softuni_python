number_of_floor = int(input())
number_of_room = int(input())

for x in range(number_of_floor, 0, -1):

    for a in range(0, number_of_room):

        if x == number_of_floor:
            print(f"L{x}{a}", end=" ")

        elif x % 2 != 0:
            print(f"A{x}{a}", end=" ")

        else:
            print(f"O{x}{a}", end=" ")

    print()



#OK