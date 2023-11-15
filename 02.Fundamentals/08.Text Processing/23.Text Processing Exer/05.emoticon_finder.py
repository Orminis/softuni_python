"""
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.
"""
text = input()

symbols = [f"{text[index]}{text[index + 1]}" for index in range(0, len(text)) if text[index] == ":"]
print("\n".join(symbols))


for index in range(0, len(text)):
    if text[index] == ":":
        print(f"{text[index]}{text[index + 1]}")