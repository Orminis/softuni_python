from math import floor

project_hours = int(input())
days_to_complete = int(input())
overtime_workers = int(input())

overtime_hours = 2

educational_time = days_to_complete * 8 * 0.1
available_time = days_to_complete * 8 - educational_time
overtime = floor(overtime_workers * overtime_hours * days_to_complete)
total_time = floor(available_time + overtime)

difference = floor(total_time - project_hours)

if difference >= 0:
    print(f'Yes!{difference} hours left.')
else:
    print(f'Not enough time!{abs(difference)} hours needed.')
