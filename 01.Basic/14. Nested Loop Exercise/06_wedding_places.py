last_sector = ord(input())
number_of_rows = int(input())
number_of_place = int(input())

counter_of_places = 0
counter_for_s = 0

for s in range(65, last_sector + 1):
    if counter_for_s != 0:
        number_of_rows += 1
    for r in range(1, number_of_rows + 1):
        if r % 2 == 0:
            for p in range(97, 97 + number_of_place + 2):
                print(f"{chr(s)}{r}{chr(p)}")
                counter_of_places += 1
        else:
            for p in range(97, 97 + number_of_place):
                print(f"{chr(s)}{r}{chr(p)}")
                counter_of_places += 1

    counter_for_s += 1

print(counter_of_places)