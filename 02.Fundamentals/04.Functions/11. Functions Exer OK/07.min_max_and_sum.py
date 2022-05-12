numbers = input().split()
numbers_as_digits = []
for x in numbers:
    numbers_as_digits.append(int(x))

print(f"The minimum number is {min(numbers_as_digits)}")
print(f"The maximum number is {max(numbers_as_digits)}")
print(f"The sum number is: {sum(numbers_as_digits)}")
