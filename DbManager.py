import psycopg2

try:
    config = psycopg2.connect(
        host="localhost",
        database="Assignment3",
        user="postgres",
        password="lpe123"
    )
    cursor = config.cursor()
    config.autocommit = True
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
        # config.commit()
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
        # config.commit()
        return True
    except Exception as e:
        print(e)


def getAllStudents():
    try:
        query = "SELECT * FROM students"
        cursor.execute(query)
        # config.commit()
        
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
        # config.commit()
    except Exception as e:
        print(e)


def updateStudentEmail(student_id, new_email):
    try:
        query = f"UPDATE students SET email = '{new_email}' \
            WHERE student_id = '{student_id}';"
        cursor.execute(query)
        # config.commit()
    except Exception as e:
        print(e)


def deleteStudent(student_id):
    try:
        query = f"DELETE FROM students \
            WHERE student_id = '{student_id}';"
        cursor.execute(query)
        # config.commit()
    except Exception as e:
        print(e)

while True:
    choice = input("Menu: \n1. Create Table\n2. Load Data\n3. Retrieve Students\n4. Add Student\n5. Update Student\n6. Delete Student\n0. Exit\n")
    if choice == "1":
        createTable()
    elif choice == "2":
        loadData()
    elif choice == "3":
        getAllStudents()
    elif choice == "4":
        fname = input("Please enter first name: ")
        lname = input("Please enter last name: ")
        email = input("Please enter email: ")
        date = input("Please enter date(yyyy-mm-dd): ")
        addStudent(fname, lname, email, date)
    elif choice == "5":
        id = input("Please enter id: ")
        email = input("Please enter email: ")
        updateStudentEmail(id, email)
    elif choice == "6":
        id = input("Please enter id: ")
        deleteStudent(id)
    elif choice == "0":
        cursor.close()
        config.close()
        break