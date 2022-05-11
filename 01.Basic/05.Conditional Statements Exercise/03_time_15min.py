hours = int(input())
minutes = int(input())
final_time = 0

final_time = (hours * 60) + minutes + 15

hours = final_time // 60
minutes = final_time % 60

if hours > 23:
    print(f"0:{minutes:02d}")
else:
    print(f"{hours}:{minutes:02d}")