# Student Management System
# Developed as part of the Python Internship
# Week 4 - Task 4: Student Management System
# Concepts: variables, input/output, conditions, loops, functions,
# dictionaries/lists, file handling, exception handling, and datetime.

import json
from datetime import datetime

DATA_FILE = "students.json"


def load_students():
    """Load student records from the JSON file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print("Warning: Data file format is invalid. Starting with an empty list.")
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: The data file is empty or damaged. Starting with an empty list.")
        return []
    except OSError as error:
        print(f"Error reading student data: {error}")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving student data: {error}")
        return False


def find_student_index(students, student_id):
    """Return the index of a student, or -1 if not found."""
    for index, student in enumerate(students):
        if student["id"].lower() == student_id.lower():
            return index
    return -1


def add_student(students):
    print("\n--- Add Student ---")
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student_index(students, student_id) != -1:
        print("A student with that ID already exists.")
        return

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))
        if age <= 0:
            print("Age must be a positive whole number.")
            return
    except ValueError:
        print("Invalid age. Please enter a whole number.")
        return

    course = input("Enter course: ").strip()
    city = input("Enter city: ").strip()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "city": city,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    students.append(student)
    if save_students(students):
        print("Student added and saved successfully.")
    else:
        print("Student added in memory, but saving failed.")


def view_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 35)
        print(f"ID:     {student['id']}")
        print(f"Name:   {student['name']}")
        print(f"Age:    {student['age']}")
        print(f"Course: {student['course']}")
        print(f"City:   {student['city']}")
        print(f"Added:  {student.get('created_at', 'Unknown')}")
    print("-" * 35)


def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter student ID to search: ").strip()
    index = find_student_index(students, student_id)

    if index == -1:
        print("Student not found.")
        return

    student = students[index]
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"City: {student['city']}")


def update_student(students):
    print("\n--- Update Student ---")
    student_id = input("Enter student ID to update: ").strip()
    index = find_student_index(students, student_id)

    if index == -1:
        print("Student not found.")
        return

    student = students[index]
    print("Press Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    age_text = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    city = input(f"City [{student['city']}]: ").strip()

    if name:
        student["name"] = name

    if age_text:
        try:
            age = int(age_text)
            if age <= 0:
                print("Age must be positive. Update cancelled.")
                return
            student["age"] = age
        except ValueError:
            print("Invalid age. Update cancelled.")
            return

    if course:
        student["course"] = course
    if city:
        student["city"] = city

    if save_students(students):
        print("Student updated successfully.")
    else:
        print("Changes made in memory, but saving failed.")


def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ").strip()
    index = find_student_index(students, student_id)

    if index == -1:
        print("Student not found.")
        return

    removed_student = students.pop(index)
    if save_students(students):
        print(f"Student {removed_student['name']} deleted successfully.")
    else:
        print("Record removed in memory, but saving failed.")


def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")


def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the Student Management System.")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
