def display_menu():
    """
     Display the main menu options for the Student Grade Analyzer.
     """

    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")


def add_student(students):
    """
      Add a new student to the system.

      Parameters:
          students (list): A list of student dictionaries,
                           where each dictionary contains:
                           - "name" (str)
                           - "grades" (list of int)

      Process:
          - Prompts user for a student name.
          - Checks for duplicates (case-insensitive).
          - Adds student if unique.
      """
    name = input("Enter student name: ").strip()

    # Check for duplicate student names
    for student in students:
        if student["name"].lower() == name.lower():
            print("A student with this name already exists.")
            return

    # Append new student
    students.append({"name": name, "grades": []})


def add_grades(students):
    """
      Add grades to an existing student.

      Parameters:
          students (list): The list of student dictionaries.

      Process:
          - Find student by name.
          - Accept integer grades 0–100 until the user enters 'done'.
          - Validate input and range.
      """

    name = input("Enter student name to add grades: ").strip()

    student = None

    # Find the student (case-insensitive)
    for s in students:
        if s["name"].lower() == name.lower():
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    print("Enter a grade (or 'done' to finish) :")

    while True:
        grade_input = input("Grade: ").strip()

        if grade_input.lower() == "done":
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Invalid input. Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")


def calculate_average(grades):
    """
      Calculate the average of a list of grades.

      Parameters:
          grades (list): A list of integers, each between 0–100.

      Returns:
          float: The average grade.

      Raises:
          ZeroDivisionError: If the grades list is empty.
      """

    if len(grades) == 0:
        raise ZeroDivisionError("Cannot compute average of empty grade list.")
    return sum(grades) / len(grades)


def show_report(students):
    """
        Display a summary report of all students and their average grades.

        Parameters:
            students (list): The list of student dictionaries.

        Output:
            - Each student's average grade.
            - Summary: max, min, and overall average across students.
        """

    if not students:
        print("No students in the system.")
        return

    print("\n--- Student Report ---")

    all_averages = []

    for student in students:
        name = student["name"]
        grades = student["grades"]

        try:
            avg = calculate_average(grades)
            all_averages.append(avg)
            print(f"{name}'s average grade is {avg:.2f}")
        except ZeroDivisionError:
            print(f"{name}'s average grade is N/A")

    if not all_averages:
        print("\nNo grades available to create a summary.")
        return

    print("\n--- Summary ---")
    print(f"Max Average: {max(all_averages):.2f}")
    print(f"Min Average: {min(all_averages):.2f}")
    print(f"Overall Average of all grades: {sum(all_averages) / len(all_averages):.2f}")


def find_top_performer(students):
    """
     Determine and display the student with the highest average grade.

     Parameters:
         students (list): The list of student dictionaries.

     Process:
         - Ignores students with no grades.
         - Uses calculate_average() to determine ranking.
     """

    if not students:
        print("No students in the system.")
        return

    try:
        # Find student with highest average; ignore empty grade lists
        top_student = max(
            students,
            key=lambda s: calculate_average(s["grades"]) if s["grades"] else float("-inf")
        )

        # Check if top student actually has grades
        if len(top_student["grades"]) == 0:
            print("There is no top student (no valid grades found).")
            return

        avg = calculate_average(top_student["grades"])
        print(f"The student with the highest average is  {top_student['name']} with grade of {avg:.2f}")

    except ValueError:
        print("Could not determine top performer student due to invalid data.")


def main():
    """
      Main program loop for the Student Grade Analyzer.

      Features:
          - Displays menu
          - Handles user choices
          - Manages student list
      """

    students: list[dict[str, list]] = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1–5).")
            continue

        if choice == 1:
            add_student(students)
        elif choice == 2:
            add_grades(students)
        elif choice == 3:
            show_report(students)
        elif choice == 4:
            find_top_performer(students)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
