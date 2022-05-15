number_of_rooms = int(input())
are_chairs_enough = True
free_chairs = 0

for room_num in range(1, number_of_rooms + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room_num}")
        are_chairs_enough = False
    else:
        free_chairs += difference

if are_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")
