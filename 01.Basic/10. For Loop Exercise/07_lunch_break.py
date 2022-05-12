from math import ceil

tv_show = str(input())
time_episode = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
free_time = break_duration / 4
left_time = break_duration - lunch_time - free_time
available_time = left_time - time_episode

if left_time >= time_episode:
    print(f"You have enough time to watch {tv_show} and left with {ceil(abs(available_time))} minutes free time.")
else:
    needed_time = time_episode - left_time
    print(f"You don't have enough time to watch {tv_show}, you need {ceil(abs(available_time))} more minutes.")