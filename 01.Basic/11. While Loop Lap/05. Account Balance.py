# account = 0
#
# while True:
#     income = input()
#     if income == "NoMoreMoney":
#         break
#
#     number = float(income)
#
#     if number < 0:
#         print("Invalid operation!")
#         break
#
#     account += number
#     print(f'Increase: {number:.2f}')
#
# print(f'Total: {account:.2f}')

##############################################################

account = 0
income = input()

while income != "NoMoreMoney":

    number = float(income)
    if number < 0:
        print("Invalid operation!")
        break

    account += number
    print(f'Increase: {number:.2f}')

    income = input()

print(f'Total: {account:.2f}')
