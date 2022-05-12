#Плодове и зеленчуци

product = input()

# if product in "banana, apple, kiwi, cherry, lemon  grapes":
#     print("fruit")
# elif product in "tomato, cucumber, pepper и carrot":
#     print('vegetable')
# else:
#     print('unknown')

if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" \
        or product == "grapes":
    print("fruit")

elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    print("vegetable")

else:
    print("unknown")
