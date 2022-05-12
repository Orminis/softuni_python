#How much will cost a fishing boat.
#Depends from the time of year: Spring - 3k; Summer / Autumn -4.2k; Winter = 2.6k
#discount - 6ppl = 10%; 7-11 = 15%; 12+ = 25%  // if fishermen are even number +5% discount except during autumn

budget = int(input())
season = input()
number_of_fishermen = int(input())

price = 0

#Checking the season
if season == "Spring":
    price = 3000
elif season == "Winter":
    price = 2600
elif season == "Summer" or season == "Autumn":
    price = 4200

if number_of_fishermen <= 6:
    price -= price * 0.10
elif 6 < number_of_fishermen <= 11:
    price -= price * 0.15
elif number_of_fishermen > 11:
    price -= price * 0.25

if number_of_fishermen % 2 == 0 and season != "Autumn":
    price -= price * 0.05

if budget < price:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
else:
    left_money = budget - price
    print(f"Yes! You have {left_money:.2f} leva left.")
