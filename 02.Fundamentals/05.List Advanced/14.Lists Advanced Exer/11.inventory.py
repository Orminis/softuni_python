collected_items = input().split(', ')
commands = input()

#
while not commands == "Craft!":
    command = commands.split(' - ')
    item = command[1]

    if command[0] == "Collect":
        if item not in collected_items:
            collected_items.append(item)
    elif command[0] == "Drop":
        if item in collected_items:
            collected_items.remove(item)
    elif command[0] == "Combine Items":
        old_item, new_item = item.split(":")
        for i in range(len(collected_items)):
            if collected_items[i] == old_item:
                collected_items.insert(i + 1, new_item)
                break
    elif command[0] == "Renew":
        for i in range(len(collected_items)):
            if collected_items[i] == item:
                collected_items.append(collected_items.pop(i))

    commands = input()


print(', '.join(collected_items))