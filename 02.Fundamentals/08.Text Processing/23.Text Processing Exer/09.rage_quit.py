data = input()

index = 0
current_string = ''
final_result = ''
while index < len(data):
    if not data[index].isdigit():
        current_string += data[index]
        index += 1
    else:
        current_number = ''
        while data[index].isdigit():
            current_number += data[index]
            index += 1
            if index == len(data):
                break
        current_number = int(current_number)
        output = current_string.upper() * current_number
        final_result += output
        current_string = ''

print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)


# unique_elements = []
# for el in final_result:
#     if el not in unique_elements:
#         unique_elements.append(el)
# print(f"Unique symbols used: {len(unique_elements)}")