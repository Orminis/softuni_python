number_of_lines = int(input())
capacity = 255                      #in liters

counter_for_water = 0               #if we successfully load a water in the tank

for line in range(number_of_lines):
    current_flow = int(input())
    if capacity - current_flow < 0:
        print("Insufficient capacity!")
    else:
        counter_for_water += current_flow
        capacity -= current_flow
print(counter_for_water)
