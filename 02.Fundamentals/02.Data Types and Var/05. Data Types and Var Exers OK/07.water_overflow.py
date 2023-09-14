"""
You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow.
On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.
"""

number_of_lines = int(input())
capacity = 255                      #in liters

counter_for_water = 0               #if we successfully load water in the tank

for line in range(number_of_lines):
    current_flow = int(input())
    if capacity - current_flow < 0:
        print("Insufficient capacity!")
    else:
        counter_for_water += current_flow
        capacity -= current_flow
print(counter_for_water)
