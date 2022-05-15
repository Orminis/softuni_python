characters = input().split(", ")

# # standard for loop
# ascii_dictionary = {}
# for i in characters:
#     ascii_number = ord(i)
#     ascii_dictionary[i] = ascii_number

# dictionary comprehension
ascii_dictionary = {k: ord(k) for k in characters}

print(ascii_dictionary)


# Dictionary comprehension #######################

print({k: ord(k) for k in input().split(", ")})