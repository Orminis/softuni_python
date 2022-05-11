import math
world_record = float(input())       # world record in seconds
distance = float(input())           # lenght of the trace
time = float(input())               # time to swim 1 meter

time_to_swim = distance * time
additional_time = math.floor(distance / 15) * 12.5       # additional seconds due to water resistance
total_time_to_swim = time_to_swim + additional_time

if total_time_to_swim < world_record:
    print(f" Yes, he succeeded! The new world record is {total_time_to_swim:.2f} seconds.")
else:
    needed_seconds = total_time_to_swim - world_record
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")