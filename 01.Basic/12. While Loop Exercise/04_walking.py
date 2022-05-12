
needed_steps = 0

while needed_steps < 10000:
    steps = input()
    if steps == "Going home":
        steps_going_home = int(input())
        needed_steps += steps_going_home
        break
    else:
        number_of_steps = int(steps)
        needed_steps += number_of_steps


if needed_steps >= 10000:
    steps_above = needed_steps - 10000
    print(f"Goal reached! Good job!")
    print(f"{steps_above} steps over the goal!")
else:
    steps_below = 10000 - needed_steps
    print(f"{steps_below} more steps to reach goal.")