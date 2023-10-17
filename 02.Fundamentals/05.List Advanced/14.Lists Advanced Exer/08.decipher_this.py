"""
You are given a secret message you should decipher. To do that, you need to know that in each word:
the second and the last letter are switched (e.g., Holle means Hello)
the first letter is replaced by its character code (e.g., 72 means H)
"""
string_of_words = input().split()

for word in string_of_words:

    numbers = [char for char in word if char.isdigit()]

    first_letter = chr(int(''.join(numbers)))
    current_word = list(first_letter + word[len(numbers):])
    current_word[1], current_word[-1] = current_word[-1], current_word[1]

    print(f'{"".join(current_word)} ', end="")
