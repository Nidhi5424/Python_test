
class InvalidGradeError(Exception):
    pass

def validate_grade(grade_str):
    assert grade_str != "", "Input cannot be empty."

    grade = int(grade_str)  

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    if grade < 40:
        raise InvalidGradeError("Failing grade! Student did not pass.")

    print("Grade is valid. Student passed.")

user_input = input("Enter student's grade (0-100): ")

try:
    validate_grade(user_input)
except AssertionError as ae:
    print("AssertionError:", ae)
except ValueError as ve:
    print("ValueError:", ve)
except InvalidGradeError as ie:
    print("InvalidGradeError:", ie)
