from peewee import *

conn = SqliteDatabase('training_db2.sqlite')


class Students(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


class Courses(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')

    class Meta:
        database = conn


class StudentCourses(Model):
    student_id = ForeignKeyField(Students, to_field="id", column_name='student_id')
    course_id = ForeignKeyField(Courses, to_field="id", column_name='courses_id')

    class Meta:
        database = conn


def students_filling(students):
    for student in students:
        user = Students(name=student[1], surname=student[2], age=student[3], city=student[4])
        user.save()


def courses_filling(courses):
    for course in courses:
        subject = Courses(name=course[1], time_start=course[2], time_end=course[3])
        subject.save()


def stud_courses_fill(student_courses):
    for i in student_courses:
        stud_course = StudentCourses(student_id=i[0], courses_id=i[1])
        stud_course.save()


def main():
    Students.create_table()
    Courses.create_table()
    StudentCourses.create_table()
    courses = [(1, "python", "21.07.21", "21.08.21"), (2, "java", "13.07.21", "16.08.21")]
    students = [(1, "Max", "Brooks", 24, "Spb"), (2, "John", "Stones", 15, "Spb"),
                (3, "Andy", "Wings", 45, "Manchester"), (4, "Kate", "Brooks", 34, "Spb")]
    student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
    students_filling(students)
    courses_filling(courses)
    stud_courses_fill(student_courses)

    age = 30
    query_1 = Students.select().where(Students.age > age)
    print(f"Students who older than {age}:")
    for student in query_1:
        print(student.name, student.surname)

    course = "python"
    query_2 = Students.select().join(StudentCourses).join(Courses).where(Courses.name == course)
    print("-" * 50)
    print(f"Students who learning {course}:")
    for student in query_2:
        print(student.name, student.surname)

    city = "Spb"
    query_3 = Students.select().join(StudentCourses).join(Courses).where((Courses.name == course) & (Students.city == city))
    print("-" * 50)
    print(f"Students who learning {course} and from {city}:")
    for student in query_3:
        print(student.name, student.surname)
    conn.close()


if __name__ == '__main__':
    main()
