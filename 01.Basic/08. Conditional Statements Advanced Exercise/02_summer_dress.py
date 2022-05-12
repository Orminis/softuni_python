# Какво облекло да облечем в зависимост от времето от денонощието и градусите
# градуси
# време от денонощието

degrees = int(input())      # 10 <= d <= 18 < d <= 24 < d <= 25
time_of_day = input()       # Morning, Afternoon, Evening.
outfit = ''
shoes = ''

#проверка по време на деня
if time_of_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees > 24:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time_of_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degrees > 24:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
