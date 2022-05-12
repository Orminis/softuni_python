sum_of_prime_nums = 0
sum_of_non_prime_nums = 0
command = input()

while command != "stop":

    number = int(command)

    if number < 0:
        print("Number is negative.")
        number = 0

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if number == 1:
        is_prime = False

    if is_prime:
        sum_of_prime_nums += number

    else:
        sum_of_non_prime_nums += number

    command = input()

print(f"Sum of all prime numbers is: {sum_of_prime_nums}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_nums}")
