# Student Management System
def add_student(name, roll):
    with open("students.txt", "a") as f:
        f.write(f"{roll},{name}\n")

def view_students():
    with open("students.txt", "r") as f:
        for line in f:
            roll, name = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}")

# Example Usage
add_student("Kowshik", "101")
view_students()
