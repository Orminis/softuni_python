x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 ** 2

wall_squares_meters = ((x * x) * 2 - door) + (((x * y) - window) * 2)
roof_squares_meters = x * y * 2 + (((x * h) / 2) * 2)

green_paint = wall_squares_meters / 3.4
red_paint = roof_squares_meters / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
