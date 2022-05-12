n = int(input())
l = int(input())

for num1 in range(1, n + 1):
    for num2 in range(1, n + 1):
        for ch1 in range(97, 97 + l):
            for ch2 in range(97, 97 + l):
                for num3 in range(1, n + 1):

                    if num3 > num2 and num3 > num1:
                        print(f"{num1}{num2}{chr(ch1)}{chr(ch2)}{num3}", end=" ")