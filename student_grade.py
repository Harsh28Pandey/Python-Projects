'''
Welcome to the Student Grade Management App
add
update
delete
view
exit

'''

# Initionally dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"added {name} with grade {grade}")

# Update a student
def update_student(name, grade):
    if(name in student_grades):
        student_grades[name] = grade
        print(f"Updated {name} with grade {grade}")
    else:
        print(f"{name} not found")
    
# Delete a student
def delete_student(name):
    if(name in student_grades):
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} not found")

def display_student():
    print("Student Grades")
    for name, grade in student_grades.items():
        print(f"{name} : {grade}")
    else:
        print("No students found/added")

def main():
    while True:
        print("Welcome to the Student Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student Grades")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        
        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_student()
        
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")
        
    
main()