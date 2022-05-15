count = int(input())

grades = {}

for _ in range(count):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

########### 1st way ###################
# filtered_grades = {}
#
# for name, grades in grades.items():
#     avg_grades = sum(grades) / len(grades)
#     if avg_grades >= 4.50:
#         filtered_grades[name] = avg_grades
#
# sorted_grades = sorted(filtered_grades.items(), key=lambda kvpt: -kvpt[1])
# for name, grade in sorted_grades:
#     print(f"{name} -> {grade:.2f}")


############ 2nd way ##################

filtered_grades = lambda f_grade: sum(f_grade[1]) / len(f_grade[1]) >= 4.50
list_of_filtered_grades = list(filter(filtered_grades, grades.items()))

filtered_dict = dict(list_of_filtered_grades)

sorted_grades = lambda s_grade: sum(s_grade[1]) / len(s_grade[1])
list_of_sorted_grades = sorted(filtered_dict.items(), key=sorted_grades, reverse=True)

sorted_dict = dict(list_of_sorted_grades)

[print(f"{name} -> {sum(grade) / len(grade):.2f}") for name, grade in sorted_dict.items()]

