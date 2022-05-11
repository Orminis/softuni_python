from math import ceil

serial_name = input()
episode_duration = int(input())
pause_duration = int(input())

lunch_time = pause_duration * 0.125
rest_time = pause_duration * 0.25
time_left = pause_duration - lunch_time - rest_time

difference = time_left - episode_duration

if difference >= 0:
    print(f"You have enough time to watch {serial_name} and left with {ceil(abs(difference))} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(abs(difference))} more minutes.")