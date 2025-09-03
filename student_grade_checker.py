# Student Grade Checker
def grade_checker(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Example Usage
marks_list = {"Kowshik": 85, "Mani": 45}
for student, marks in marks_list.items():
    print(f"{student}: {grade_checker(marks)}")
