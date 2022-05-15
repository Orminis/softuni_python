# numbers = ''
# letters = ''
# characters = ''
#
# text = input()
#
# for char in text:
#     if char.isdigit():
#         numbers += char
#     elif char.isalpha():
#         letters += char
#     else:
#         characters += char
#
# print(numbers)
# print(letters)
# print(characters)

# ###############################

txt = input()
separator = "\n"
print(separator.join([''.join(filter(lambda x: x.isdigit(), txt)),
                      ''.join(filter(lambda x: x.isalpha(), txt)),
                      ''.join(filter(lambda x: not x.isalpha() and not x.isdigit(), txt))
                      ]))
