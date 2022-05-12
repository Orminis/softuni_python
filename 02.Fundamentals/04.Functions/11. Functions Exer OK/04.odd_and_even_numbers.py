def get_even_and_odd_numbers(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_even_digits, sum_of_odd_digits


number_as_string = input()
even_sum, odd_sum = get_even_and_odd_numbers(number_as_string)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
