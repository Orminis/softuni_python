# Да се принтира коя комбинация от 2 числа дава резултат равен на 3то число


first_num = int(input())
second_num = int(input())
third_num = int(input())
is_equal = False
counter = 0

for i in range (first_num, second_num + 1):
    for j in range (first_num, second_num + 1):
        counter += 1

        if i + j == third_num:
            is_equal = True
            print(f"Combination N:{counter} ({i} + {j} = {third_num})")

            break
    if is_equal:
        break

if not is_equal:
    print(f"{counter} combinations - neither equals {third_num}")
