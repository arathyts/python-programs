from abc import ABC, abstractmethod


# Abstract Class
class Evaluation(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass


# Base Class
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Derived Class
class Student(Person, Evaluation):

    student_count = 0

    def __init__(self, name, age, roll_number, marks):
        Person.__init__(self, name, age)

        self.roll_number = roll_number
        self.marks = marks

        Student.student_count += 1

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate average marks
    def calculate_average(self):
        return self.calculate_total() / 3

    # Implement abstract method
    def calculate_grade(self):

        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    # Static Method
    @staticmethod
    def validate_marks(mark):

        if 0 <= mark <= 100:
            return True
        else:
            return False

    # Operator Overloading
    # Compare students based on total marks
    def __lt__(self, other):
        return self.calculate_total() < other.calculate_total()

    # Display student details
    def display(self):

        print("Name        :", self.get_name())
        print("Age         :", self.get_age())
        print("Roll Number :", self.roll_number)
        print("Marks       :", self.marks)
        print("Total Marks :", self.calculate_total())
        print("Average     :", round(self.calculate_average(), 2))
        print("Grade       :", self.calculate_grade())

    # Class Method
    @classmethod
    def display_student_count(cls):

        print("\nTotal number of students created:",
              cls.student_count)


# Sports Class
class Sports:

    def __init__(self, sports_score):

        self.sports_score = sports_score

    def display_sports_score(self):

        print("Sports Score:", self.sports_score)


# Multiple Inheritance
class Result(Student, Sports):

    def __init__(self, name, age, roll_number, marks, sports_score):

        Student.__init__(
            self,
            name,
            age,
            roll_number,
            marks
        )

        Sports.__init__(
            self,
            sports_score
        )

    # Final score
    def calculate_final_score(self):

        return self.calculate_total() + self.sports_score

    # Display final result
    def display(self):

        Student.display(self)

        self.display_sports_score()

        print("Final Score :", self.calculate_final_score())


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("==============================================")
print("      STUDENT RANK LIST MANAGEMENT SYSTEM")
print("==============================================")


# Ask number of students
while True:

    try:

        n = int(input("\nEnter the number of students: "))

        if n > 0:
            break
        else:
            print("Please enter a positive number.")

    except ValueError:

        print("Please enter a valid number.")



students = []

for i in range(n):

    print("\n----------------------------------------------")
    print("Enter details of Student", i + 1)
    print("----------------------------------------------")

    # Name
    name = input("Enter name: ")

    # Age
    while True:

        try:

            age = int(input("Enter age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than 0.")

        except ValueError:

            print("Please enter a valid age.")


    # Roll Number
    while True:

        try:

            roll_number = int(input("Enter roll number: "))
            break

        except ValueError:

            print("Please enter a valid roll number.")


    # Marks in 3 subjects
    marks = []

    for j in range(3):

        while True:

            try:

                mark = int(
                    input(
                        f"Enter marks for Subject {j + 1}: "
                    )
                )

                # Static method validation
                if Student.validate_marks(mark):

                    marks.append(mark)
                    break

                else:

                    print(
                        "Invalid marks. "
                        "Marks must be between 0 and 100."
                    )

            except ValueError:

                print("Please enter a valid mark.")


    # Sports score
    while True:

        try:

            sports_score = int(
                input("Enter sports score: ")
            )

            if sports_score >= 0:
                break
            else:
                print("Sports score cannot be negative.")

        except ValueError:

            print("Please enter a valid sports score.")


    # Create Result object
    student = Result(
        name,
        age,
        roll_number,
        marks,
        sports_score
    )

    # Add object to list
    students.append(student)



# DISPLAY STUDENT DETAILS
# ------------------------------------------

print("\n\n==============================================")
print("             STUDENT DETAILS")
print("==============================================")


for student in students:

    print("\n----------------------------------------------")

    student.display()


# SORT STUDENTS
# ------------------------------------------

# Operator overloading __lt__ is used here
# Sorting based on total marks

students.sort(reverse=True)


# DISPLAY RANK LIST
# ------------------------------------------

print("\n\n==============================================")
print("                FINAL RANK LIST")
print("==============================================")


print(
    f"{'Rank':<8}"
    f"{'Roll No':<10}"
    f"{'Name':<20}"
    f"{'Total':<10}"
    f"{'Average':<10}"
    f"{'Grade':<8}"
)


print("-" * 66)


for rank, student in enumerate(students, start=1):

    print(
        f"{rank:<8}"
        f"{student.roll_number:<10}"
        f"{student.get_name():<20}"
        f"{student.calculate_total():<10}"
        f"{student.calculate_average():<10.2f}"
        f"{student.calculate_grade():<8}"
    )


# TOTAL NUMBER OF STUDENTS
# ------------------------------------------

Student.display_student_count()


print("\n==============================================")
print("          Rank List Generated Successfully")
print("==============================================")