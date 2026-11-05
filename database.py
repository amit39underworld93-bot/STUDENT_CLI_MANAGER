import psycopg 

def get_connection():
    return psycopg.connect(

        host = "localhost",
        port = 5432,
        dbname = "student_manager",
        user = "postgres",
        password = "AmitKum!290"

    )

connection = get_connection()


