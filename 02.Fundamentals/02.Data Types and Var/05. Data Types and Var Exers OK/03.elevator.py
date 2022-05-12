from math import ceil

number_of_ppl = int(input())
elevator_capacity = int(input())
courses = 0

if elevator_capacity != 0:
    courses = ceil(number_of_ppl / elevator_capacity)
print(courses)

