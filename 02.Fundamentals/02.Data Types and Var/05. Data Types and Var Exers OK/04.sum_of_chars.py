# Calculate the sum of characters' ASCII numbers.

number_of_characters = int(input())

sum_of_ascii_values = 0
for i in range(number_of_characters):
    next_character = input()
    sum_of_ascii_values += ord(next_character)

print(f"The sum equals: {sum_of_ascii_values}")
