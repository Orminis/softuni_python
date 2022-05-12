hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

exam_time_in_minutes = (hour_of_exam * 60) + minutes_of_exam
arrival_time_in_minutes = (hour_of_arrival * 60) + minutes_of_arrival

diff = abs(exam_time_in_minutes - arrival_time_in_minutes)

hour = diff // 60
minutes = diff % 60

if exam_time_in_minutes == arrival_time_in_minutes:
    print('On time')

elif exam_time_in_minutes > arrival_time_in_minutes:
    if diff <= 30:
        print('On time')
        print(f'{minutes} minutes before the start')
    elif 30 < diff < 60:
        print('Early')
        print(f'{minutes} minutes before the start')
    elif diff > 59:
        print('Early')
        print(f'{hour}:{minutes:02d} hours before the start')

elif exam_time_in_minutes < arrival_time_in_minutes:
    print("Late")

    if diff < 60:
        print(f'{minutes} minutes after the start')
    elif diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
