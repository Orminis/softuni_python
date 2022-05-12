number_of_jury = int(input())
all_grades = 0
current_grades = 0
grade_counter = 0

while True:
    name_of_presentation = input()
    if name_of_presentation == "Finish":
        print(f"Student's final assessment is {all_grades / grade_counter:.2f}.")
        break

    for x in range(number_of_jury):
        grade = float(input())
        current_grades += grade
        all_grades += grade
        grade_counter += 1

    print(f"{name_of_presentation} - {current_grades / number_of_jury:.2f}.")
    current_grades = 0