# Student CLI Manager 🎓

A robust, terminal-based Student Management System built with Python and PostgreSQL.
This application provides a comprehensive Command-Line Interface (CLI) to seamlessly manage student records, subjects, academic marks, and automated result calculations.

# 🚀 Features

- **Full CRUD Operations:** Create, Read, Update, and Delete student profiles and subject details directly from the terminal.

- **Relational Database Integration:** Uses psycopg to connect with a PostgreSQL database, utilizing SQL JOIN operations to link students, subjects, and marks.

- **Automated Grading System:** Automatically calculates total marks, percentages, and assigns grades (A+, A, B, C, D, F) based on academic performance.

- **Search Functionality:** Quickly find specific students using keyword-based search (ILIKE query for case-insensitive matching).

- **Robust Error Handling:** Validates user inputs (e.g., catching ValueError for age/marks) to prevent application crashes during execution.

# 🛠️ Tech Stack
- **Language:** Python 3

- **Database:** PostgreSQL

- **Driver/Connector:** psycopg (psycopg3)

# 🗄️ Database Setup 

Before running the application, ensure you have PostgreSQL installed and running.

**1. Create a database named student_manager:**

   CREATE DATABASE student_manager;

**2. Create the required tables:**

   *Run the following SQL queries in your PostgreSQL terminal (psql) or pgAdmin:*
   
   *-- Create Students Table:*
   
   **CREATE TABLE students (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       age INT NOT NULL,
       email VARCHAR(100) UNIQUE,
       course VARCHAR(100)
   );**
   
   *-- Create Subjects Table:*
   
   **CREATE TABLE subjects (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL UNIQUE
   );**
   
   *-- Create Marks Table:*
   
   **CREATE TABLE marks (
       student_id INT REFERENCES students(id) ON DELETE CASCADE,
       subject_id INT REFERENCES subjects(id) ON DELETE CASCADE,
       marks INT CHECK (marks >= 0 AND marks <= 100),
       PRIMARY KEY (student_id, subject_id)
   );**

**Note:** *Update the database credentials (user, password) in the database.py file to match your local PostgreSQL configuration.*

# 💻 How to Run (Installation & Execution)

**1. Clone the repository:**

git clone https://github.com/amit39underworld93-bot/STUDENT_CLI_MANAGER.git cd STUDENT_CLI_MANAGER

**2. Install dependencies:**

   Install the required PostgreSQL adapter for Python using the provided requirements file.

   *pip install -r requirements.txt*

**3. Execute the application:**

   *python3 main.py*

# 📸 Usage Overview

Upon launching the application, you will be greeted with the following interactive menu:

========================================
         STUDENT CLASS MANAGER
========================================
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
6. Add marks
7. View student's marks
8. Calculate result
9. Update marks
10. View all subjects
11. Add subject
12. Update subject
13. Exit

Enter your choice between 1 to 13:
