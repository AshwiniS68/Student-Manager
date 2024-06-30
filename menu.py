students = []

def add_student():
    student_id = int(input("Enter student ID: "))  
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))
    student_info = {"student_id": student_id, "student_name": student_name, "student_age": student_age}
    students.append(student_info)
    print(f"Student {student_name} added successfully!")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print(f"Student with ID {student_id} deleted successfully!")
            break
    else:
        print(f"Student with ID {student_id} not found.")

def update_student():
    student_id = int(input("Enter student ID to update: ")) 
    for student in students:
        if student["student_id"] == student_id:
            student_name = input("Enter updated student name: ") 
            student_age = int(input("Enter updated student age: ")) 
            student["student_name"] = student_name
            student["student_age"] = student_age
            print(f"Student with ID {student_id} updated successfully!")
            break
    else:
        print(f"Student with ID {student_id} not found.")

def view_all_students():
    print("\nStudent Records:")
    for student in students:
        print(f"ID: {student['student_id']}, Name: {student['student_name']}, Age: {student['student_age']}")

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View All Students")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
