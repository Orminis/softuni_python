def get_grade_score():
    number = float(input())
    if 2 < number or number > 6:
        return "None"
    if number <= 2.99:
        return "Fail"
    elif number <= 3.49:
        return "Poor"
    elif number <= 4.49:
        return "Good"
    elif number <= 5.49:
        return "Very Good"
    elif number <= 6.00:
        return "Excellent"


grade = get_grade_score()
print(grade)


###################################

def get_grade_score():
    number = float(input())
    if number <= 2.99:
        return "Fail"
    elif number <= 3.49:
        return "Poor"
    elif number <= 4.49:
        return "Good"
    elif number <= 5.49:
        return "Very Good"
    elif number <= 6.00:
        return "Excellent"


grade = get_grade_score()
print(grade)
