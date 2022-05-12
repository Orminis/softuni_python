number = int(input())
# from 97 to 122 in ASCII Table
if number <= 26:
    for first_symbol in range(number):
        for second_symbol in range(number):
            for third_symbol in range(number):
                print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")



# number = int(input())
#
# for i in range(number + 1, -1):
#     i = int(i)
#     temp_value = ''
#     for x in (0, i + 1):
#         pass
#not finished need to think it
