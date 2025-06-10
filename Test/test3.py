students = {}

while True:
    print("\nWelcome to the Student Data Organizer")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case 1:
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            subjects = input("Subjects (comma-separated): ").split(',')

            students[student_id] = {
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": [s.strip() for s in subjects]
            }

            print("Student added successfully!")

        case 2:
            if not students:
                print("No student data available.")
            else:
                print("\n--- Student Information ---")
                for sid, info in students.items():
                    print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']} | Subjects: {', '.join(info['subjects'])}")

        case 3:
            student_id = input("Enter Student ID to update: ")
            if student_id in students:
                print("Enter new details (leave blank to keep current):")
                name = input(f"Name ({students[student_id]['name']}): ") or students[student_id]['name']
                age = input(f"Age ({students[student_id]['age']}): ") or students[student_id]['age']
                grade = input(f"Grade ({students[student_id]['grade']}): ") or students[student_id]['grade']
                subjects = input(f"Subjects ({', '.join(students[student_id]['subjects'])}): ")

                students[student_id] = {
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subjects": [s.strip() for s in subjects.split(',')] if subjects else students[student_id]['subjects']
                }

                print("Student updated successfully!")
            else:
                print("Student not found.")

        case 4:
            student_id = input("Enter Student ID to delete: ")
            if student_id in students:
                del students[student_id]
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        case 5:
            all_subjects = set()
            for info in students.values():
                all_subjects.update(info['subjects'])

            if all_subjects:
                print("Subjects Offered:")
                print(", ".join(sorted(all_subjects)))
            else:
                print("No subjects found.")

        case 6:
            print("Thank you for using the Student Data Organizer!")
            break

        case _:
            print("Invalid choice. \nPlease enter a number from 1 to 6.")
