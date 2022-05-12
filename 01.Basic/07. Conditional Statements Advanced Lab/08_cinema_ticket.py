#Цена на билет за кино в зависимост от ден от седмицата

# day_of_week = input()
#
# if day_of_week == "Saturday" or day_of_week == "Sunday":
#     print('16')
# elif day_of_week == "Wednesday" or day_of_week == "Thursday":
#     print('14')
# elif day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
#     print('12')

day_of_week = input()

if day_of_week in "Saturday Sunday":
    print('16')
elif day_of_week in "Wednesday Thursday":
    print('14')
elif day_of_week in "Monday Tuesday Friday":
    print('12')