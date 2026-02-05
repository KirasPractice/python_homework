import sqlite3

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

#CREATE TABLES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        student_id INTERGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTERGER,
        major TEXT        
    )               
    """)
                   

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
        instructor_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students (student_id),
        FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    )
    """)

    print("Tables created successfully.")


# Connect to the database

def add_student(cursor, name, age, major):
    try:
        cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
    except sqlite3.IntegrityError:
        print(f"{name} is already in teh database")


def add_course(cursor, name, instructor):
    try:
        cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


    # Insert sample data into tables

add_student(cursor, 'Akira', 24, 'Computer Science')
add_student(cursor, 'Bob', 22, 'History')
add_student(cursor, 'Charlie', 19, 'Biology')
add_course(cursor, 'Math 101', 'Dr. Smith')
add_course(cursor, 'English 101', 'Ms. Jones')
add_course(cursor, 'Chemistry 101', 'Dr. Lee')

conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
print("Sample data inserted successfully.")

#Within Python, SQL SELECT statements are executed like the INSERT statements, but you also need to retrieve the results.  Add the following to your school_b.py program:


cursor.execute("SELECT * FROM Students WHERE name = 'Akira'")
result = cursor.fetchall()
for row in result:
    print(row)
print("row retrieved")


def enroll_student(cursor, student, course):
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    results = cursor.fetchall()
    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return
    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    results = cursor.fetchall()
    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return
    cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

    ... # And at the bottom of your "with" block

enroll_student(cursor, "Akira", "Math 101")
enroll_student(cursor, "Akira", "Chemistry 101")
enroll_student(cursor, "Bob", "Math 101")
enroll_student(cursor, "Bob", "English 101")
enroll_student(cursor, "Charlie", "English 101")
conn.commit() # more writes, so we have to commit to make them final!