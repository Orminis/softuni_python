"""
On the first line, you will be given an integer n representing the number of rooms in the business center.
On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
For example: "XXXXX 4" (5 chairs and 4 visitors).
Keep track of the free chairs:
The rooms start from 1.
If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
Otherwise, print: "Game On, {total_free_chairs} free chairs left"
"""
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
