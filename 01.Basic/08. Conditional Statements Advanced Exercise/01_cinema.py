# Cinema: to calculate income as per type of movie screening and number of seats in the hall
# type of movie screening
# row
# columns

movie_screening = input()       # type: Premiere; Normal; Discount
hall_row = int(input())         # full number
hall_column = int(input())      # full number

income = 0

full_hall = hall_row * hall_column

# Calculation of income
if movie_screening == "Premiere":
    income = full_hall * 12.00

elif movie_screening == "Normal":
    income = full_hall * 7.50

elif movie_screening == "Discount":
    income = full_hall * 5.00
# format till 2 digit after .
print(f"{income:.2f} leva")
