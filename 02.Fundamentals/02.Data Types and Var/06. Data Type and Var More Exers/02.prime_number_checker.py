number = int(input())
is_prime = True

if number > 1:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            is_prime = False
            break
print(is_prime)