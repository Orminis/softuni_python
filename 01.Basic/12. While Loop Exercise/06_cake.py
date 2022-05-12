width = int(input())
lenght = int(input())
cake_size = width * lenght

while cake_size > 0:
    current_pieces_of_cake = input()

    if current_pieces_of_cake == "STOP":
        break

    cake_size -= int(current_pieces_of_cake)

if cake_size > 0:
    print(f"{cake_size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")