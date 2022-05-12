import math


def coordination_point(x1, y1):
    diagonal_to_o = math.sqrt(x1 ** 2 + y1 ** 2)
    return diagonal_to_o


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if coordination_point(x1, y1) <= coordination_point(x2, y2):
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")
