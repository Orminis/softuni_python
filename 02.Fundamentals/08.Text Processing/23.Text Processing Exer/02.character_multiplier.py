"""
Create a program which receives two strings on a single line separated by a single space and
prints the sum of their multiplied character codes as follows:
multiply str1[0] with str2[0] and add the result to the total sum,
then continue with the next two characters.
If one of the strings is longer than the other,
add the remaining character codes to the total sum without multiplication.
"""

def multiply_ascii_char_nums(shorter_lst, longer_lst):
    multiply_sum = 0
    for i in range(len(shorter_lst)):
        multiply_sum += shorter_lst[i] * longer_lst[i]
    return multiply_sum


def additional_sum(long_list, short_list):
    add_sum = sum(long_list[len(short_list):])
    return add_sum


def from_symbols_to_ascii_numbers(strings):
    list_data = []
    for index in strings:
        list_data.append(ord(index))
    return list_data


data_strings = input().split()

total_sum = 0
list_data1 = from_symbols_to_ascii_numbers(data_strings[0])
list_data2 = from_symbols_to_ascii_numbers(data_strings[1])

if len(list_data1) > len(list_data2):
    total_sum += multiply_ascii_char_nums(list_data2, list_data1)
    total_sum += additional_sum(list_data1, list_data2)
else:
    total_sum += multiply_ascii_char_nums(list_data1, list_data2)
    total_sum += additional_sum(list_data2, list_data1)
print(total_sum)