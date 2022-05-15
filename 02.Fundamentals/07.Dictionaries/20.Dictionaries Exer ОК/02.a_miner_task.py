bag_with_treasures = {}

resource = input()

while resource != "stop":
    quantity = int(input())

    if resource not in bag_with_treasures:
        bag_with_treasures[resource] = 0
    bag_with_treasures[resource] += quantity

    resource = input()

for k, v in bag_with_treasures.items():
    print(f"{k} -> {v}")
