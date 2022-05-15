text = input()

symbols = [f"{text[index]}{text[index + 1]}" for index in range(0, len(text)) if text[index] == ":"]
print("\n".join(symbols))


for index in range(0, len(text)):
    if text[index] == ":":
        f"{text[index]}{text[index + 1]}"