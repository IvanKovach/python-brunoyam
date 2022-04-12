import sqlite3


def create_database(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name Varchar(32), "
                       "surname Varchar(32), age int, city Varchar(32))")
    except sqlite3.OperationalError:
        print(f"Table students already exists, skipping creating")
    try:
        cursor.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name Varchar(32), "
                       "time_start timestamp, time_end timestamp)")
    except sqlite3.OperationalError:
        print(f"Table courses already exists, skipping creating")
    try:
        cursor.execute("CREATE TABLE student_courses (student_id int, course_id int, "
                   "FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(course_id) REFERENCES courses(id))")
    except sqlite3.OperationalError:
        print(f"Table student_courses already exists, skipping creating")
    conn.close()


def base_filling(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    try:
        courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
        students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
                    (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
        student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", students)
        cursor.executemany("INSERT INTO courses VALUES (?, ?, ?, ?)", courses)
        cursor.executemany("INSERT INTO student_courses VALUES (?, ?)", student_courses)
        conn.commit()
    except sqlite3.IntegrityError:
        print("This data already in database, skipping")
    conn.close()


def get_students_older_than(dbname, age):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    request = "SELECT name, surname FROM students WHERE age > " + str(age)
    cursor.execute(request)
    students = cursor.fetchall()
    conn.close()
    return students


def get_students_on_course(dbname, course):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    request = "SELECT students.name, students.surname FROM students, courses, student_courses WHERE " \
              "students.id = student_courses.student_id AND courses.id = student_courses.course_id AND" \
              " courses.name = '" + course + "'"
    cursor.execute(request)
    students = cursor.fetchall()
    conn.close()
    return students


def get_students_on_course_from(dbname, course, city):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    request = "SELECT students.name, students.surname FROM students, courses, student_courses WHERE " \
              "students.id = student_courses.student_id AND courses.id = student_courses.course_id AND" \
              " courses.name = '" + course + "'" + " AND students.city = '" + city + "'"
    cursor.execute(request)
    students = cursor.fetchall()
    conn.close()
    return students


def main():
    db_name = 'training_db.sqlite'
    create_database(db_name)
    base_filling(db_name)

    age = 30
    print("-" * 50)
    print(f"Students who older than {age}:")
    for student in get_students_older_than(db_name, age):
        print(student[0], student[1])

    course = 'python'
    print("-" * 50)
    print(f"Students who learning {course}:")
    for student in get_students_on_course(db_name, course):
        print(student[0], student[1])

    city = 'Spb'
    print("-" * 50)
    print(f"Students who learning {course} and from {city}:")
    for student in get_students_on_course_from(db_name, course, city):
        print(student[0], student[1])


if __name__ == '__main__':
    main()
