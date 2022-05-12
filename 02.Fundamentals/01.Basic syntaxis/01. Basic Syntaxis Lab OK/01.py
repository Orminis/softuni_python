



#решение с проверки
number_one = int(input())
number_two = int(input())
number_three = int(input())

if number_one > number_two and number_one > number_three:
    print(number_one)
elif number_two > number_one and number_two > number_three:
    print(number_two)
else:
    print(number_three)

#решение с for цикъл
import sys
biggest_num = -sys.maxsize
current_num = int(input())
for a in range(2):
    if current_num > biggest_num:
        biggest_num = current_num
    current_num = int(input())
print(biggest_num)

#лесно решение
a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))