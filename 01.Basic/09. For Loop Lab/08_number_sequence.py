import sys

n = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize

for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")