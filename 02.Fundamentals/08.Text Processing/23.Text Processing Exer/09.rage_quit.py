"""
Every gamer knows what rage-quitting means. It’s basically when you’re just not good enough and you blame everybody else for losing a game.
You press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.

Peter is a gamer, and a bad one at that. He asks for your help; he wants to be the most annoying kid in his team,
so when he rage-quits he wants something truly spectacular.
He’ll give you a series of strings followed by non-negative numbers, e.g., "a3";
 you need to print on the console each string repeated N times; convert the letters to uppercase beforehand.
In the example, you need to write back "AAA".

On the output, print first a statistic of the number of unique symbols used (the casing of letters is irrelevant, meaning that 'a' and 'A' are the same);
the format should be "Unique symbols used {0}". Then, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with a string and for each string there will be a corresponding number.
The entire input will be given on a single line; Peter is too lazy to make your job easier.
"""
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