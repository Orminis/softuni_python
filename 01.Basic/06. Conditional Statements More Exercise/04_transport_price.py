number_kilometers = int(input())
part_of_the_day = input()

taxi_starting_price = 0.70
taxi_day_tariff = 0.79          # per kilometer
taxi_night_tariff = 0.90        # per kilometer
bus_tariff = 0.09               # per kilometer every part of the day
train_tariff = 0.06

bus_price = bus_tariff * number_kilometers
train_price = train_tariff * number_kilometers

if part_of_the_day == "day":  #price for taxi depending of the part of the day
    taxi_price = taxi_starting_price + taxi_day_tariff * number_kilometers
else:
    taxi_price = taxi_starting_price + taxi_night_tariff * number_kilometers

if number_kilometers < 20:
    cheapest_transport = taxi_price
elif number_kilometers < 100:
    cheapest_transport = min(bus_price,taxi_price)
else:
    cheapest_transport = min(train_price,bus_price,taxi_price)

print(f"{cheapest_transport:.2f}")