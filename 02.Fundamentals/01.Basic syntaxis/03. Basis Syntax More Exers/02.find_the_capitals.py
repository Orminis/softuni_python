# How to iterate through a string to find the capital letters indexes and print them as list

string = input("lets find the capital letters = ")

capital_letters_list = []
for index in range(len(string)):
    if string[index].isupper():
        capital_letters_list.append(index)

print(capital_letters_list)
