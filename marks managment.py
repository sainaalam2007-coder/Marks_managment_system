# Marks Management System - Mini Project

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # dictionary {subject: marks}

    def total_marks(self):
        return sum(self.marks.values())

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def grade(self):
        avg = self.average_marks()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

    def __str__(self):
        return (f"Roll No: {self.roll_no}, Name: {self.name}, "
                f"Total: {self.total_marks()}, Average: {self.average_marks():.2f}, "
                f"Grade: {self.grade()}")


class MarksManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name, marks):
        if roll_no in self.students:
            print("❌ Roll number already exists!")
        else:
            self.students[roll_no] = Student(roll_no, name, marks)
            print("✅ Student added successfully!")

    def display_all(self):
        if not self.students:
            print("No records found.")
        else:
            for student in self.students.values():
                print(student)

    def search_student(self, roll_no):
        student = self.students.get(roll_no)
        if student:
            print(student)
        else:
            print("❌ Student not found!")

    def update_marks(self, roll_no, subject, new_marks):
        student = self.students.get(roll_no)
        if student:
            student.marks[subject] = new_marks
            print("✅ Marks updated successfully!")
        else:
            print("❌ Student not found!")


# ---------------- MAIN PROGRAM ----------------
def main():
    system = MarksManagementSystem()

    while True:
        print("\n--- Marks Management System ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            subjects = int(input("Enter number of subjects: "))
            marks = {}
            for i in range(subjects):
                subject = input(f"Enter subject {i+1} name: ")
                score = int(input(f"Enter marks for {subject}: "))
                marks[subject] = score
            system.add_student(roll_no, name, marks)

        elif choice == "2":
            system.display_all()

        elif choice == "3":
            roll_no = input("Enter Roll No to search: ")
            system.search_student(roll_no)

        elif choice == "4":
            roll_no = input("Enter Roll No: ")
            subject = input("Enter subject name: ")
            new_marks = int(input("Enter new marks: "))
            system.update_marks(roll_no, subject, new_marks)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()