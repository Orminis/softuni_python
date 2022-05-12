month = input()
count_nights = int(input())
studio = 0
apartment = 0
total_price_studio = 0
total_price_apartment = 0

if month == 'May' or month == 'October':
    if 14 >= count_nights > 7:
        total_price_apartment = count_nights * 65
        studio = count_nights * 50
        total_price_studio = studio - studio * 0.05

    elif count_nights > 14:
        studio = count_nights * 50
        total_price_studio = studio - studio * 0.3
        apartment = count_nights * 65
        total_price_apartment = apartment - apartment * 0.1

    else:
        total_price_studio = count_nights * 50
        total_price_apartment = count_nights * 65

if month == 'June' or month == 'September':
    if count_nights > 14:
        studio = count_nights * 75.20
        total_price_studio = studio - studio * 0.2
        apartment = count_nights * 68.70
        total_price_apartment = apartment - apartment * 0.1
    else:
        total_price_studio = count_nights * 75.20
        total_price_apartment = count_nights * 68.70

if month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    total_price_studio = count_nights * studio
    total_price_apartment = count_nights * apartment
    if count_nights > 14:
        total_price_apartment = total_price_apartment - total_price_apartment * 0.1

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')