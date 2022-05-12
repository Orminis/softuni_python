numbers_of_range = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(numbers_of_range):
    current_number = int(input())

    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1


p1 /= numbers_of_range / 100
p2 /= numbers_of_range / 100
p3 /= numbers_of_range / 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
