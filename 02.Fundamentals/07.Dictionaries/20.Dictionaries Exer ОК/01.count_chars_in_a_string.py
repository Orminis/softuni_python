my_dict = {}
characters = input()

# for char in characters:
#     string = characters.split()
#
#     if char not in my_dict and char != " ":
#         my_dict[char] = 1
#
#     elif char in my_dict and char != " ":
#         my_dict[char] += 1
#
# for key, value in my_dict.items():
#     print(f"{key} -> {value}")


for char in characters:
    string = characters.split()

    if char != " ":
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    else:
        pass
for key, value in my_dict.items():
    print(f"{key} -> {value}")
