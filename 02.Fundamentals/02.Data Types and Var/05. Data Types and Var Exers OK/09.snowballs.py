snowballs_number = int(input())

max_snowball_value = 0
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0

for snowball in range(snowballs_number):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = pow(snowball_weight / snowball_time, snowball_quality)

    if current_snowball_value > max_snowball_value:
        max_snowball_value = current_snowball_value
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality


print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")