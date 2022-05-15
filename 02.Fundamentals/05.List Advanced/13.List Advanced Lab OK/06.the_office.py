# employees_happiness = input().split()
# happiness_improvement_factor = int(input())
# multiplied_happiness = []
# sum = 0
# happy_count = 0
#
# for i in employees_happiness:
#     mapped = int(i) * happiness_improvement_factor
#     multiplied_happiness.append(mapped)
#     sum += mapped
# average_happiness = sum / len(employees_happiness)
#
# for i in multiplied_happiness:
#     if i >= average_happiness:
#         happy_count += 1
#
# if happy_count >= len(employees_happiness) / 2:
#     print(f"Score: {happy_count}/{len(employees_happiness)}. Employees are happy!")
# else:
#     print(f"Score: {happy_count}/{len(employees_happiness)}. Employees are not happy!")

####################################################################################################

happiness = [int(el) for el in input().split()]
# happiness = list(map(lambda el: int(el), input().split()))

factor = int(input())

multiplied_happiness_by_factor = [num * factor for num in happiness]
# multiplied_happiness_by_factor_map = list(map(lambda x: x * factor, happiness))

average_happiness = sum(multiplied_happiness_by_factor) / len(multiplied_happiness_by_factor)

happy_employees = [i for i in multiplied_happiness_by_factor if i >= average_happiness]
# happy_employees_filtered = list(filter(lambda i: i >= average_happiness, multiplied_happiness_by_factor))

half_n = len(multiplied_happiness_by_factor) / 2
if len(happy_employees) >= half_n:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_by_factor)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_by_factor)}. Employees are not happy!")
