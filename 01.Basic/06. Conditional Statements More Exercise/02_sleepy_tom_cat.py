resting_days = int(input())

working_days = 365 - resting_days

playtime = (resting_days * 127) + (working_days * 63)
diff = abs(30000 - playtime)
hours = diff // 60
min = diff % 60

if playtime > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {min} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours} hours and {min} minutes less for play")