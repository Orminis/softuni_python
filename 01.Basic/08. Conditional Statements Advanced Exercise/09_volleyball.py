import math

type_of_year = input()  #leap or normal
number_of_holidays = int(input())        #number of hollidays
number_of_weekends = int(input())        #weekends which vladi travels to hometown

number_of_games = ((48 - number_of_weekends) * 3 / 4) + number_of_weekends + (number_of_holidays * 2 / 3)
if type_of_year == "leap":
    number_of_games += number_of_games * 0.15

print(math.floor(number_of_games))
