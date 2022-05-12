"""You will be given the coordinates of four points.
 The first and the second pair of points form two different lines.
 Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting
 from the point which is closer to the center of the coordinate system (0, 0).
You can reuse the method that you wrote for the previous problem.
If the lines are of equal length, print only the first one.
The resulting coordinates must be formatted to the lower integer."""


import math


def coordination_line(lst):
    x1,y1,x2,y2 = map(float, lst)
    diagonal = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
    return diagonal


def coordination_point(lst):
    x1,y1,x2,y2 = map(float, lst)
    first_point_to_o = math.sqrt(x1 ** 2 + y1 ** 2)
    second_point_to_o = math.sqrt(x2 ** 2 + y2 ** 2)
    if first_point_to_o <= second_point_to_o:
        return print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        return print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")


coordinates = [input() for x in range(8)]
first_line = coordinates[:4]
second_line = coordinates[4:]

if coordination_line(first_line) >= coordination_line(second_line):
    coordination_point(first_line)
else:
    coordination_point(second_line)