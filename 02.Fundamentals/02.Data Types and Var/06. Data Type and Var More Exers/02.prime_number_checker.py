num = int(input())
is_prime = True

if num > 1:
    for i in range(2, num // 2):
        if num % i == 0:
            is_prime = False
            print(num, "is not a prime number")
            print(f"{i} times {num // i} is {num}")
            break
print(is_prime)