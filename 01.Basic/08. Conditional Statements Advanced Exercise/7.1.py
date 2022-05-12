# Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# # 4. Броят рам памет - цяло число в интервала [1…100]

budget_peter = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

price_all_video_cards = video_cards_count * 250
price_per_processor = price_all_video_cards * 0.35
price_per_ram = price_all_video_cards * 0.10

price_all_processors = price_per_processor * processors_count
price_all_ram = price_per_ram * ram_count

sum_all_components = price_all_processors + price_all_ram + price_all_video_cards

if video_cards_count > processors_count:
    sum_all_components -= sum_all_components * 0.15

difference = abs(budget_peter - sum_all_components)

if budget_peter >= sum_all_components:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
