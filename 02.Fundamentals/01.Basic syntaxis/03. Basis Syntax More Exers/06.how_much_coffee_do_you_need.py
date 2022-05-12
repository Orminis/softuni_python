coffee_count = 0
command = input()

while True:
    if command == "DOG" or command == "CAT" or command == "CODING" or command == "MOVIE":
        coffee_count += 2
    elif command == "dog" or command == "cat" or command == "coding" or command == "movie":
        coffee_count += 1
    if coffee_count > 5:
        print("You need extra sleep")
        break
    elif command == "END":
        print(coffee_count)
        break

    command = input()
