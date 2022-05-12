counter = 0
number_of_tickets = 0

standard = 0
student = 0
kid = 0


while True:
    name_of_movie = input()

    if name_of_movie == 'Finish':
        break
    number_of_seats = int(input())

    while True:
        type_of_ticket = input()

        if type_of_ticket == "End":
            break

        counter += 1
        number_of_tickets += 1

        if type_of_ticket == "standard":
            standard += 1
        elif type_of_ticket == "kid":
            kid += 1
        elif type_of_ticket == "student":
            student += 1

        if counter >= number_of_seats:
            break
    print(f"{name_of_movie} - {(counter / number_of_seats) * 100:.2f}% full.")
    counter = 0
    number_of_seats = 0

print(f"Total tickets: {number_of_tickets}")
print(f"{(student / number_of_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / number_of_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / number_of_tickets) * 100:.2f}% kids tickets.")