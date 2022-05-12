# Do not let the wolf who pretends to be sheep to eat any sheep.
# If the wolf is in the beginning (end of the list) shoo it away.
# If the wolf is inside the herd warn the sheep in front of the wolf (the one with higher index).
# there will be only 1 wolf.

data_list = input().split(", ")

for i in data_list:
    if i == "wolf":
        if data_list.index(i) == len(data_list) - 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            sheep_position = len(data_list) - 1 - data_list.index(i)
            print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
            break


wolf_sheep_queue = input().split(", ")

if wolf_sheep_queue[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index in range(0, len(wolf_sheep_queue)):
        if wolf_sheep_queue[-(index + 1)] == "wolf":
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")