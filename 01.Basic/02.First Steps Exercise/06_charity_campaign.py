# Calculate gathered sum for charity campaign after expenses.

day_of_event = int(input())
number_of_confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

#Sum per confectioner per day
price_per_cake = cakes * 45
price_for_waffles = waffles * 5.8
price_per_pancake = pancakes * 3.2
net_profit_per_confectioner = price_per_cake + price_for_waffles + price_per_pancake
total_profit_per_day = net_profit_per_confectioner * number_of_confectioners
total_event_sum = total_profit_per_day * day_of_event
final_sum = total_event_sum - (total_event_sum / 8)
print(final_sum)