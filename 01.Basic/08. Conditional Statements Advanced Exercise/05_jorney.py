#Where to take vacation as per budget and season

budget = float(input())
season = input()


if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        location_price = budget * 0.3
    elif season == "winter":
        location_price = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        location_price = budget * 0.4
    elif season == "winter":
        location_price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    location_price = budget * 0.9

if season == "winter" or destination == "Europe":
    location = 'Hotel'
else:
    location = "Camp"

print(f"Somewhere in {destination}")
print(f"{location} - {location_price:.2f}")
