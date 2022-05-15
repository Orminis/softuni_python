def multiply_ascii_char_nums(list1, list2):
    multiply_sum = 0
    for i in range(len(list1)):
        multiply_sum += list1[i] * list2[i]
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