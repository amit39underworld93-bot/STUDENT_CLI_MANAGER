from database import get_connection

def add_student():
    print("\n====== ADD STUDENTS ======")
    name = input("Enter the name of the student: ").strip()

    while True:
        try:
            age = int(input("Enter the age of the student: "))
            break
        except ValueError:
            print("Please enter a valid numeric value for age!!!")
    email = input("Enter the email address: ")
    course = input("Enter the course of the student: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """INSERT INTO STUDENTS (name, age, email, course) VALUES (%s, %s, %s, %s)"""

    cursor.execute(query, (name, age, email, course))

    connection.commit()
    cursor.close()
    connection.close()

    print("\nSTUDENT ADDED SUCCESSFULLY!!!")

# ==================================================================================================================================================================

def view_student():
    print("\n====== ALL STUDENTS ======")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT id, name, age, email, course FROM students ORDER BY id""")

    students = cursor.fetchall()

    if not students:
        print("\nNO STUDENTS FOUND ")

    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Age: {student[2]} | "
                f"Email: {student[3]} | "
                f"Course: {student[4]}"
            )

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def search_student():
    print("\n====== SEARCH STUDENTS ======")

    keyword = input("Enter student's name: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    query = """ SELECT id, name, age, email,course FROM students WHERE name ILIKE %s ORDER BY id"""

    cursor.execute(query, (f"%{keyword}%", ))

    students = cursor.fetchall()

    if not students:
            print("\nNO STUDENTS FOUND")

    else:
            for student in students:
                print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Age: {student[2]} | "
                f"Email: {student[3]} | "
                f"Course: {student[4]}"
            )

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def update_student():
    print("\n====== UPDATE STUDENTS ======")

    name = input("Enter student's name: ").strip()

    while True:
        try:
            id = int(input("Enter student's id: "))
            age = int(input("Enter student's age: "))
            break
        except ValueError:
            print("Please enter a valid numeric value for age!!!")

    email = input("Enter student's email: ").strip()
    course = input("Enter student's course: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    query = """UPDATE students SET name = %s, age = %s, email = %s, course = %s WHERE id = %s"""

    cursor.execute(query, (name, age, email, course, id))

    if cursor.rowcount == 0:
        print("\nSTUDENT NOT FOUND")

    else:
        connection.commit()
        print("\nSTUDENT UPDATED SUCCESSFULLY!!!")

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def delete_student():
    print("\n====== DELETE STUDENTS ======")

    while True: 
        try:
            student_id = int(input("Enter student's id: "))
            break
        except ValueError:
            print("Please enter a vaid numeric value for id!!!")

    confirmation = input("Are you sure? (y/n): ")

    if confirmation != "y":
        print("\nDELETE CANCELLED")
        return

    connection = get_connection()
    cursor = connection.cursor()

    query = """DELETE FROM students WHERE id = %s"""
    cursor.execute(query, (student_id, ))

    if cursor.rowcount == 0:
        print("\nSTUDENT NOT FOUND")

    else:
        connection.commit()
        print("\nSTUDENT DELETED SUCCESSFULLY!!!")

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def add_marks():
    print("\n====== ADD MARKS ======")

    while True:
        try:
            student_id = int(input("Enter student's id: "))
            subject_id = int(input("Enter subject's id: "))
            marks = int(input("Enter marks(0-100): "))
            break
        except Exception:
            print("Please enter a valid numeric value!!!")

    connection = get_connection()
    cursor = connection.cursor()

    query = """INSERT INTO marks (student_id, subject_id, marks) VALUES (%s, %s, %s)"""

    try:
        cursor.execute(query, (student_id, subject_id, marks))
        connection.commit()

        print("\nMARKS ADDED SUCCESSFULLY!!!")

    except Exception as error:
        connection.rollback()
        print("Except", error)

    finally:
        cursor.close()
        connection.close()

# ==================================================================================================================================================================

def update_marks():
    print("\n====== UPDATE STUDENTS's MARKS ======")

    while True:
        try:
            student_id = int(input("Enter student's id: "))
            subject_id = int(input("Enter subject's id: "))
            marks  = int(input("Enter student's marks: "))
            break
        except ValueError:
            print("Please enter a valid numeric value!!!")

    connection = get_connection()
    cursor = connection.cursor()

    query = """UPDATE marks SET marks = %s WHERE student_id = %s AND subject_id = %s"""

    cursor.execute(query, (marks, student_id, subject_id))

    if cursor.rowcount == 0:
        print("\nMARKS NOT FOUND(check if student id and subject id is correct)")

    else:
        connection.commit()
        print("\nMARKS UPDATED SUCCESSFULLY!!!")

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def view_marks():
    print("\n======= VIEW MARKS ======")

    while True:
        try:
            student_id = int(input("Enter student's id: "))
            break
        except ValueError:
            print("Please enter a valid numeric value!!!")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            students.name,
            subjects.name,
            marks.marks
        FROM marks
        JOIN students
            ON marks.student_id = students.id
        JOIN subjects
            ON marks.subject_id = subjects.id
        WHERE students.id = %s
        ORDER BY subjects.id
    """

    cursor.execute(query, (student_id, ))

    result = cursor.fetchall()

    if not result:
        print("\nNO MARKS FOUND ")

    else:
        print(f"\n Student: {result[0][0]}")

        for row in result:
            print(f"Subject: {row[1]}" , "," , f"\nMarks: {row[2]}")

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def calculate_result():

    print("\n====== STUDENT RESULT ======")

    while True:
        try:
            student_id = int(input("Enter student's id: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    connection = get_connection()
    cursor = connection.cursor()

    query = """SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id = subjects.id WHERE marks.student_id = %s"""

    cursor.execute(query, (student_id, ))

    result = cursor.fetchall()

    if not result:
        print("\nNO MARKS FOUND")
        cursor.close()
        connection.close()

        return

    total = sum(row[1] for row in result)
    maximum = len(result) * 100
    percentage = (total/maximum) * 100

    print("\n====== RESULT ======")

    for subject, marks in result:

        print(f"{subject}, {marks}")

    print(f"\nTotal: {total}/{maximum}")
    print(f"Percentage: {percentage}")

    if percentage > 90:
        grade = "A+"

    elif percentage > 80:
        grade = "A"

    elif percentage > 70:
        grade = "B"

    elif percentage > 60:
        grade = "C"

    elif percentage > 50:
        grade = "D"

    else:
        grade = "F"

    print(f"Grade = {grade}")

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def view_subjects():
    print("\n====== ALL SUBJECTS ======")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT id, name FROM subjects ORDER BY id""")

    subjects = cursor.fetchall()

    if not subjects:
        print("\nNO SUBJECTS FOUND")

    else:
        for subject in subjects:
            print(
                f"ID: {subject[0]} | "
                f"Name: {subject[1]} | "
            )

    cursor.close()
    connection.close()

# ==================================================================================================================================================================

def add_subjects():
    print("\n====== ADD SUBJECTS ======")
    name = input("Enter the name of the subject: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    query = """INSERT INTO SUBJECTS (name) VALUES (%s)"""

    cursor.execute(query, (name,))

    connection.commit()
    cursor.close()
    connection.close()

    print("\nSUBJECT  ADDED SUCCESSFULLY!!!")

# ==================================================================================================================================================================

def update_subject():
    print("\n====== UPDATE SUBJECTS ======")

    while True:
        try:
            id = int(input("Enter subject's id: "))
            break
        except ValueError:
            print("Please enter a valid numeric value for id!!!")

    name = input("Enter subject's name: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    query = """UPDATE subjects SET name = %s WHERE id = %s"""

    cursor.execute(query, (name, id))

    if cursor.rowcount == 0:
        print("\nSUBJECT NOT FOUND")

    else:
        connection.commit()
        print("\nSUBJECT UPDATED SUCCESSFULLY!!!")

    cursor.close()
    connection.close()