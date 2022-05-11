lenght = int(input())
width = int(input())
height = int(input())
percentage_occupied_volume = float(input())

#Volume in litters
volume_of_tank = lenght * width * height / 1000

percentage_occupied_volume /= 100

needed_litters = volume_of_tank * (1 - percentage_occupied_volume)
print(needed_litters)
