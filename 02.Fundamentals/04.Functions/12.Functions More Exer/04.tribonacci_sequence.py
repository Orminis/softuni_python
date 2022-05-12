def printtribrec(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return (printtribrec(n - 1) +
                printtribrec(n - 2) +
                printtribrec(n - 3))


def printtrib(n):
    for i in range(1, n):
        print(printtribrec(i), " ", end="")


# Driver code
n = int(input())
printtrib(n)
