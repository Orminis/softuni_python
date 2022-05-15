# data = [el.strip() for el in input().split()]
#
# alphabet = {chr(96 + num): num for num in range(1, 27)}
#
# total_sum = 0
# current_number = ''
# current_list = []
# for i in range(len(data)):
#     for char in data[i]:
#         if not char.isdigit():
#             current_list.append(char)
#         else:
#             current_number += char
#
#     current_number = int(current_number)
#     if current_list[0].isupper():
#         current_sum = current_number / alphabet.get(current_list[0].lower())
#     else:
#         current_sum = current_number * alphabet.get(current_list[0])
#
#     if current_list[1].isupper():
#         current_sum -= alphabet.get(current_list[1].lower())
#     else:
#         current_sum += alphabet.get(current_list[1])
#     total_sum += current_sum
#     current_number = ''
#     current_list = []
#
# print(f"{total_sum:.2f}")


# data = [el.strip() for el in input().split()]
#
# alphabet = {chr(96 + num): num for num in range(1, 27)}
# final_result = 0
# for i in data:
#     first_letter = i[0]
#     second_letter = i[len(i) - 1:]
#     num = int(i[1:len(i) - 1])
#
#     if first_letter.isupper():
#         current_sum = num / alphabet[first_letter.lower()]
#     else:
#         current_sum = num * alphabet[first_letter.lower()]
#
#     if second_letter.isupper():
#         current_sum -= alphabet[second_letter.lower()]
#     else:
#         current_sum += alphabet[second_letter.lower()]
#     final_result += current_sum
# print(f"{final_result:.2f}")

from string import ascii_lowercase


def extra_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for symbol in range(len(text)):
        if text[symbol].isalpha():
            index = ascii_lowercase.index(text[symbol].lower()) + 1

            if symbol == 0:
                if text[symbol] == text[symbol].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[symbol] == text[symbol].lower():
                    result += index
                else:
                    result -= index
    return result


def letter_change_number(data):
    result = 0
    for num in data:
        result += extra_func(num)

    print(f"{result:.2f}")


data = input().split()
letter_change_number(data)
