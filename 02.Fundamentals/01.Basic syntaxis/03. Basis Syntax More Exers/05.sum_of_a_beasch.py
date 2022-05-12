beach_info = input().lower()

count = 0
sand_count = beach_info.count("sand")
water_count = beach_info.count("water")
fish_count = beach_info.count("fish")
sun_count = beach_info.count("sun")

if sun_count > 0 or water_count > 0 or fish_count > 0 or sand_count > 0:
    count = sun_count + sand_count + water_count + fish_count

print(count)