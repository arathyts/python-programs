import copy

print("STUDENT RECORD MANAGEMENT SYSTEM")

# 1. Get number of students
# ------------------------------------------

try:
    n = int(input("Enter the number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0.")

    # Lists to store student details
    names = []
    roll_numbers = []
    marks = []
    # 2. Input student details
    # ------------------------------------------

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Enter Name: ").strip()

        if name == "":
            raise ValueError("Name cannot be empty.")

        roll_number = int(input("Enter Roll Number: "))

        # Input marks
        mark1 = int(input("Enter marks for Subject 1: "))
        mark2 = int(input("Enter marks for Subject 2: "))
        mark3 = int(input("Enter marks for Subject 3: "))

        # Check marks range
        if not (0 <= mark1 <= 100 and
                0 <= mark2 <= 100 and
                0 <= mark3 <= 100):
            raise ValueError("Marks must be between 0 and 100.")

        # Store data
        names.append(name)
        roll_numbers.append(roll_number)
        marks.append([mark1, mark2, mark3])
    # 3. Display stored data
    # ------------------------------------------

    print("\n==========================================")
    print("STUDENT DETAILS")
    print("==========================================")

    print("Names:", names)
    print("Roll Numbers:", roll_numbers)
    print("Marks:", marks)
    # 4. Dictionary using zip()
    # ------------------------------------------

    student_dictionary = dict(zip(roll_numbers, names))

    print("\nDictionary using zip():")
    print(student_dictionary)
    # 5. String Operations
    # ------------------------------------------

    # Convert all names to uppercase
    uppercase_names = [name.upper() for name in names]

    print("\nNames in Uppercase:")
    print(uppercase_names)

    # Names longer than 5 characters
    long_names = [name for name in names if len(name) > 5]

    print("\nNames longer than 5 characters:")
    print(long_names)

    # Count names starting with A
    a_count = sum(1 for name in names if name.upper().startswith("A"))

    print("\nNumber of names starting with 'A':")
    print(a_count)
    # 6. List Comprehension
    # ------------------------------------------

    # Students whose average marks are greater than 75
    high_average_students = [
        names[i]
        for i in range(n)
        if sum(marks[i]) / len(marks[i]) > 75
    ]

    print("\nStudents with average marks greater than 75:")
    print(high_average_students)

    # Even roll numbers
    even_roll_numbers = [
        roll for roll in roll_numbers
        if roll % 2 == 0
    ]

    print("\nEven Roll Numbers:")
    print(even_roll_numbers)

    # ------------------------------------------
    # 7. Tuple
    # ------------------------------------------

    first_student_marks = tuple(marks[0])

    print("\nFirst student's marks as Tuple:")
    print(first_student_marks)
    # 8. Set of unique marks
    # ------------------------------------------

    unique_marks = set()

    for student_marks in marks:
        unique_marks.update(student_marks)

    print("\nUnique marks from all students:")
    print(unique_marks)
    # 9. Shallow Copy and Deep Copy
    # ------------------------------------------

    shallow_copy = copy.copy(marks)
    deep_copy = copy.deepcopy(marks)

    # Modify original marks
    marks[0][0] = 100

    print("\n==========================================")
    print("COPY DEMONSTRATION")
    print("==========================================")

    print("\nOriginal Marks:")
    print(marks)

    print("\nShallow Copy:")
    print(shallow_copy)

    print("\nDeep Copy:")
    print(deep_copy)

    print("\nNote:")
    print("Shallow copy reflects the change because nested lists")
    print("are still shared.")
    print("Deep copy does not reflect the change because it has")
    print("completely independent nested lists.")

# 10. Error Handling
# ------------------------------------------

except ValueError as e:
    print("\nInvalid input:", e)

except Exception as e:
    print("\nUnexpected error occurred:", e)

finally:
    print("\n==========================================")
    print("_____completed-______.")
    print("==========================================")