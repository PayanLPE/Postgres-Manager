import psycopg2

try:
    config = psycopg2.connect(
        host="localhost",
        database="Assignment3",
        user="postgres",
        password="lpe123"
    )
    cursor = config.cursor()
    print("Database connected successfully")
except Exception as e:
    print("Database not connected successfully")


def createTable():
    try:
        query = "CREATE TABLE students (  \
                student_id SERIAL PRIMARY KEY,  \
                first_name TEXT NOT NULL,  \
                last_name TEXT NOT NULL,  \
                email TEXT NOT NULL UNIQUE,  \
                enrollment_date DATE);"
        cursor.execute(query)
        config.commit()
        return True
    except Exception as e:
        print(e)


def loadData():
    try:
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES \
                ('John', 'Doe', 'john.doe@example.com', '2023-09-01'), \
                ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), \
                ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"
        cursor.execute(query)
        config.commit()
        return True
    except Exception as e:
        print(e)


def getAllStudents():
    try:
        query = "SELECT * FROM students"
        cursor.execute(query)
        config.commit()
        
        students = cursor.fetchall()
        [print(s) for s in students]
        print("\n")
        
        return students
    except Exception as e:
        print(e)


def addStudent(first_name, last_name, email, enrollment_date):
    try:
        query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) \
            VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');"
        cursor.execute(query)
    except Exception as e:
        print(e)


def updateStudentEmail(student_id, new_email):
    try:
        query = f"UPDATE students SET email = '{new_email}' \
            WHERE student_id = '{student_id}';"
        cursor.execute(query)
        config.commit()
    except Exception as e:
        print(e)


def deleteStudent(student_id):
    try:
        query = f"DELETE FROM students \
            WHERE student_id = '{student_id}';"
        cursor.execute(query)
        config.commit()
    except Exception as e:
        print(e)

# createTable()
# loadData()
# getAllStudents()

# getAllStudents()
# addStudent("Peien", "Liu", "peienliu@cmail.carleton.ca", "2021-09-01")
# print("\n")
# getAllStudents()

# getAllStudents()
# updateStudentEmail(1,  "jd@cmail.carleton.ca")
# print("\n")
# getAllStudents()

getAllStudents()
deleteStudent(4)
print("\n")
getAllStudents()

cursor.close()
config.close()