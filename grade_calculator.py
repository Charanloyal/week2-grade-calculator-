# ---------------------------------------------------------
# Step 1: Project Setup
# File: grade_calculator.py
# Author: Charan
# Description: A program to calculate student grades, statistics, 
#              and manage student data with a menu system.
# ---------------------------------------------------------

import sys # Used to exit the program safely

# Color codes for Step 6 (ANSI Escape Codes)
# These make the text colorful in the terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Global list to store all student data (Step 3 & 4 storage)
student_records = []

# ---------------------------------------------------------
# Step 2: Define Grading System
# ---------------------------------------------------------
def calculate_grade(average):
    """Determines the letter grade based on the average marks."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_comment(grade):
    """Returns a comment based on the letter grade."""
    if grade == 'A':
        return "Excellent work! Keep it up."
    elif grade == 'B':
        return "Good job, but there's room for improvement."
    elif grade == 'C':
        return "You passed, but try harder next time."
    elif grade == 'D':
        return "You barely passed. You need to study more."
    else:
        return "Failed. Please seek extra help."

# ---------------------------------------------------------
# Step 3 & 4: Get Student Information & Collect Data
# ---------------------------------------------------------
def add_students():
    print(f"\n{CYAN}--- Add New Students ---{RESET}")
    
    while True:
        try:
            # Step 3: Validate input is a positive number
            count = int(input("How many students do you want to add? "))
            if count > 0:
                break
            print(f"{RED}Error: Please enter a number greater than 0.{RESET}")
        except ValueError:
            print(f"{RED}Error: Invalid input. Please enter a number.{RESET}")

    # Step 4: Loop to collect data
    for i in range(count):
        print(f"\nProcessing Student {i + 1}/{count}")
        name = input("Enter student name: ")
        
        marks = []
        subjects = ["Math", "Science", "English"]
        
        for subject in subjects:
            while True:
                try:
                    score = float(input(f"Enter marks for {subject} (0-100): "))
                    if 0 <= score <= 100:
                        marks.append(score)
                        break
                    print(f"{RED}Error: Marks must be between 0 and 100.{RESET}")
                except ValueError:
                    print(f"{RED}Error: Please enter a number.{RESET}")
        
        # Step 5: Calculate Results immediately
        average = sum(marks) / len(marks)
        grade = calculate_grade(average)
        comment = get_grade_comment(grade)
        
        # Store everything in a dictionary (a specialized list item)
        student = {
            "name": name,
            "marks": marks,
            "average": average,
            "grade": grade,
            "comment": comment
        }
        student_records.append(student)
        print(f"{GREEN}Student '{name}' added successfully!{RESET}")

# ---------------------------------------------------------
# Step 6: Display Results
# ---------------------------------------------------------
def display_all_students():
    if not student_records:
        print(f"\n{YELLOW}No records found. Please add students first.{RESET}")
        return

    print(f"\n{CYAN}--- Class Results ---{RESET}")
    # Printing a table header
    print(f"{'Name':<15} {'Avg':<10} {'Grade':<10} {'Comment'}")
    print("-" * 60)
    
    for student in student_records:
        # Step 6: Color coding
        color = GREEN if student['grade'] == 'A' else RED if student['grade'] == 'F' else RESET
        
        print(f"{color}{student['name']:<15} {student['average']:<10.2f} {student['grade']:<10} {student['comment']}{RESET}")

# ---------------------------------------------------------
# Step 7: Add Features (Search, Save, Menu)
# ---------------------------------------------------------
def search_student():
    search_name = input("\nEnter name to search: ").lower()
    found = False
    for student in student_records:
        if search_name in student['name'].lower():
            print(f"\n{GREEN}Found: {student['name']} - Grade: {student['grade']} ({student['average']:.2f}){RESET}")
            found = True
    if not found:
        print(f"{RED}Student not found.{RESET}")

def save_to_file():
    try:
        with open("week2/results.txt", "w") as f:
            f.write("Name, Average, Grade\n")
            for student in student_records:
                f.write(f"{student['name']}, {student['average']:.2f}, {student['grade']}\n")
        print(f"\n{GREEN}Results saved to 'week2/results.txt'{RESET}")
    except FileNotFoundError:
        # Fallback if folder doesn't exist
        with open("results.txt", "w") as f:
            f.write("Name, Average, Grade\n")
            for student in student_records:
                f.write(f"{student['name']}, {student['average']:.2f}, {student['grade']}\n")
        print(f"\n{GREEN}Results saved to 'results.txt'{RESET}")

def main_menu():
    while True:
        print(f"\n{CYAN}=== GRADE CALCULATOR MENU ==={RESET}")
        print("1. Add Students")
        print("2. Display All Results")
        print("3. Search for a Student")
        print("4. Save Results to File")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_students()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            save_to_file()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

# Start the program
if __name__ == "__main__":
    main_menu()