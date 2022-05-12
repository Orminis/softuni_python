# Решаване на задачи за изпит

failed_threshold = int(input())  # Максимална бройка оценки които са незадоволителни

failed_times = 0   # Брой на всяка оценка под 4
solved_tasks_count = 0 # Брой на решените задачи
grades_sum = 0
last_problem = ""

while True:
    name_of_problem = input()
    if name_of_problem == "Enough":
        break

    grade = int(input())

    if grade <= 4:
        failed_times += 1

        if failed_times >= failed_threshold:
            break

    last_problem = name_of_problem
    solved_tasks_count += 1
    grades_sum += grade

if failed_times < failed_threshold:
    average_grade = grades_sum / solved_tasks_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_tasks_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {failed_times} poor grades.")