# Program which shows which number is special or no. Special numbers are when the sum of its digits is 5, 7 or 11.

n = int(input())

for i in range(1, n + 1):                   #'for loop' to check every number till "n"
    temp_num = i
    sum_of_digits = 0

    while temp_num > 0:                     #Taking last digit of number and adding it to sum_of_digits
        digit = temp_num % 10
        sum_of_digits += digit
        temp_num = temp_num // 10           #Removing the last digit which was already taken from the number

    isSpecial = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11   #Check is the number special or not
    print(f"{i} -> {isSpecial}")



