name_of_student = input()
assessment = float(input())

assessment_sum = 0
counter_for_years = 0
counter_for_bad_assessments = 0

while True:
    if assessment >= 4:
        assessment_sum += assessment
        counter_for_years += 1

    elif assessment < 4:
        counter_for_bad_assessments += 1

        if counter_for_bad_assessments == 2:
            counter_for_years += 1
            print(f'{name_of_student} has been excluded at {counter_for_years} grade')
            break

    if counter_for_years == 12:
        average_grade = assessment_sum / 12
        print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
        break

    assessment = float(input())
