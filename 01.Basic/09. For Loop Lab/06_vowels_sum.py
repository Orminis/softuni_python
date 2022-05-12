text = input()

total_sum = 0
for char in text:
    if char == "a":
        total_sum += 1
    elif char == "e":
        total_sum += 2
    elif char == 'i':
        total_sum += 3
    elif char == 'o':
        total_sum += 4
    elif char == 'u':
        total_sum += 5
print(total_sum)