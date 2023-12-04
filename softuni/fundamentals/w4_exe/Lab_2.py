grade = float(input())

def grade_check(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.5:
        return "Good"
    elif grade < 5.5:
        return "Very Good"
    else:
        return "Excellent"

print(grade_check(grade))