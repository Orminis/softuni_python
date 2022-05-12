hour = int(input())
day_of_week = input()

if hour < 10 or hour >= 18 or day_of_week == "Sunday":
    print('closed')
else:
    print('open')