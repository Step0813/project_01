# Задача 4.1.
# Домашнее задание на SQL

import sqlite3

def get_connection():
    connection = sqlite3.connect('homeworks/teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_dbversion():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT sqlite_version();')
        db_version = cursor.fetchone()
        print('Вы подключились к SQLite версии: ', db_version)
        close_connection(connection)
    except(Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)

def update_exp(exp, school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = 'UPDATE Teacher SET Experience = ? WHERE School_Id = ?'
        cursor.execute(sqlquery, (exp, school_id))
        connection.commit()
        close_connection(connection)
    except(Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)

def get_school_data(school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = 'SELECT * FROM School WHERE School_Id = ?'
        cursor.execute(sqlquery, (school_id,))
        records = cursor.fetchall()
        print('Данные по школе')
        for i in records:
            print('ID школы: ', i[0])
            print('Название школы: ', i[1])
            print('Количество мест: ', i[2])
        close_connection(connection)
    except(Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)

def get_teacher_data(teacher_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = 'SELECT * FROM Teacher WHERE Teacher_Id = ?'
        cursor.execute(sqlquery, (teacher_id,))
        records = cursor.fetchall()
        print('Данные по учителю')
        for i in records:
            print('ID Учителя: ', i[0])
            print('Имя учителя: ', i[1])
            print('ID школы: ', i[2])
            print('Дата начала работы: ', i[3])
            print('Специализация: ', i[4])
            print('Зарплата: ', i[5])
            print('Опыт работы:: ', i[6])
        close_connection(connection)
    except(Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)


# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer (Primary key), Student_Name - Text, School_Id - Integer

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4


# connection = sqlite3.connect('homeworks/teachers.db')
# cursor = connection.cursor()
# sqlquery = '''INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');
# '''
# cursor.execute(sqlquery)
# connection.commit()
# connection.close()


# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

def get_student_data(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = 'SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?'
        cursor.execute(sqlquery, (student_id,))
        records = cursor.fetchall()
        for i in records:
            print('ID Студента: ', i[0])
            print('Имя студента: ', i[1])
            print('ID школы: ', i[2])
            print('Название школы: ', i[3])
        close_connection(connection)
    except(Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)


get_student_data(204)