class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        calculated_circumference = Circle.__pi * self.diameter
        return calculated_circumference

    def calculate_area(self):
        calculated_area = Circle.__pi * (self.radius ** 2)
        return calculated_area

    def calculate_area_of_sector(self, angle):
        sector_area = (angle / 360) * Circle.__pi * (self.radius ** 2)
        return sector_area


diameter = float(input())
angle = float(input())

circle = Circle(diameter)

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")