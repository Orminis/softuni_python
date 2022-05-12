# Цена за апартамент или студио в зависимост от месеца и броя нощувки
# В зависимост от месеца и броя нощувки има отстъпки

month = input()             # Въвеждаме месеца May, June, July, August, September или October;
overnights = int(input())    # Брой нощувки

cost_for_apartment = 0
cost_for_studio = 0
discount_for_apartment = 0
discount_for_studio = 0

if month == "May" or month == "October":
    cost_for_apartment = 65
    cost_for_studio = 50

    if 7 < overnights <= 14:
        discount_for_studio = cost_for_studio * 0.05

    elif overnights > 14:
        discount_for_studio = cost_for_studio * 0.30

elif month == "June" or month == "September":
    cost_for_apartment = 68.70
    cost_for_studio = 75.20

    if overnights > 14:
        discount_for_studio = cost_for_studio * 0.20

elif month == "July" or month == "August":
    cost_for_apartment = 77
    cost_for_studio = 76

if overnights > 14:
    discount_for_apartment = cost_for_apartment * 0.10

price_for_apartment = (cost_for_apartment - discount_for_apartment) * overnights
price_for_studio = (cost_for_studio - discount_for_studio) * overnights

print(f"Apartment: {price_for_apartment:.2f} lv.\nStudio: {price_for_studio:.2f} lv.")
