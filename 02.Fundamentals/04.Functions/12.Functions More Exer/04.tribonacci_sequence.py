# def printtribrec(n):
#     if n == 0 or n == 1 or n == 2:
#         return 0
#     elif n == 3:
#         return 1
#     else:
#         return (printtribrec(n - 1) +
#                 printtribrec(n - 2) +
#                 printtribrec(n - 3))
#
#
# def printtrib(n):
#     for i in range(1, n):
#         print(printtribrec(i), " ", end="")
#
#
# # Driver code
# n = int(input())
# printtrib(n)


# with memory cache optimization
# fib_cache = {0: 0, 1:1}
#
# def fib(n):
#     if n in fib_cache:  # Base case
#         return fib_cache[n]
#
#     fib_cache[n] = fib(n - 1) + fib(n - 2)  # Recursive case
#     return fib_cache
#
# [fib(n) for n in range(60)]
# result = [v for v in fib_cache.values()]
# print(result)

fib_cache = []

n = int(input("Input number: "))

for i in range(n):
    if i == 0 or i == 1:
        fib_cache.append(i)
        continue
    fib_cache.append(fib_cache[-1] + fib_cache[-2])
print(fib_cache)