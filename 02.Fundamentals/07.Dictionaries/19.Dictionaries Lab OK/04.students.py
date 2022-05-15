# Will receive some students with id and course. At the end to print the info of these students from specific
# course which will be received at the end.

searched_courses = None
courses = {}

while True:
    student_info = input()

    if ":" not in student_info:
        searched_courses = student_info
        break

    command_args = student_info.split(":")
    name = command_args[0]
    id = command_args[1]
    course = command_args[2]

    if course not in courses:
        courses[course] = {}

    courses[course][id] = name

searched_courses = searched_courses.replace("_", " ")

current_course = courses[searched_courses]
for k, v in current_course.items():
    print(f"{v} - {k}")
