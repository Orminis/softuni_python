"""
Nakov likes Math. But he also likes the English alphabet a lot. He invented a game with numbers and letters from the English alphabet. The game was simple.

You get a string consisting of a number between two letters.
Depending on whether the letter was in front of the number or after it you would perform different mathematical operations on the number to achieve the result.

First you start with the letter before the number.
If it's uppercase you divide the number by the letter's position in the alphabet.
If it's lowercase you multiply the number with the letter's position in the alphabet.
Then you move to the letter after the number.
If it's uppercase you subtract its position from the resulted number.
If it's lowercase you add its position to the resulted number.

But the game became too easy for Nakov really quick.
He decided to complicate it a bit by doing the same but with multiple strings keeping track of only the total sum of all results.
Once he started to solve this with more strings and bigger numbers it became quite hard to do it only in his mind.
So he kindly asks you to write a program that calculates the sum of all numbers after the operations on each number have been done.

For example, you are given the sequence "A12b s17G":
We have two strings – "A12b" and "s17G". We do the operations on each and sum them.
We start with the letter before the number on the first string.
A is Uppercase and its position in the alphabet is 1. So we divide the number 12 with the position 1 (12/1 = 12).
Then we move to the letter after the number. b is lowercase and its position is 2. So we add 2 to the resulted number (12+2=14).
Similarly, for the second string s is lowercase and its position is 19 so we multiply it with the number (17*19 = 323).
Then we have Uppercase G with position 7, so we subtract it from the resulted number (323 – 7 = 316).
Finally, we sum the 2 results, and we get 14 + 316=330.
"""
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
