n = int(input())

# 1 do n
# повтаряне: печатам числото + променяме (n *2 + 1)
# стоп: числото > n
# продължавам: числото <= n
number = 1
while number <= n:
    print(number)
    number = number * 2 + 1
