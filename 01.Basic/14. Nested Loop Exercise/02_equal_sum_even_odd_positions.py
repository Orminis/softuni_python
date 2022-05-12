n1 = int(input())
n2 = int(input())
odd_nums = 0
even_nums = 0


for num in range(n1, n2 + 1):
    current_num = str(num)

    for x in range(len(current_num)):
        if x % 2 == 0:
            even_nums += int(current_num[x])
        else:
            odd_nums += int(current_num[x])

    if even_nums == odd_nums:
        print(current_num, end=" ")
    even_nums = 0
    odd_nums = 0
