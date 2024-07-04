import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

# Создание объекта для выполнения SQL-запросов
cursor = db.cursor()

# Запрос INSERT для students
sql_students = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL)"
cursor.execute(sql_students, ('Kirill', 'Zharoff'))
student_id = cursor.lastrowid  # Получаем id добавленной записи

# Запрос INSERT для books
sql_books = (
    "INSERT INTO books (title, taken_by_student_id) "
    "VALUES (%s, %s), (%s, %s)"
)
val_books = ('Python book', student_id, 'SQL book', student_id)
cursor.execute(sql_books, val_books)

# Запрос INSERT для groups
sql_groups = (
    "INSERT INTO `groups` (title, start_date, end_date) "
    "VALUES (%s, %s, %s)"
)
cursor.execute(sql_groups, ('Groupa_Beta_1', '2000-01-01', '2022-01-01'))
group_id = cursor.lastrowid  # Получаем id добавленной записи

# Запрос UPDATE для students
sql_update_students = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(sql_update_students, (group_id, student_id))

# Запрос SELECT для вывода данных о студенте и его группе
sql_select_student = """
SELECT students.name, students.second_name, `groups`.title
FROM students
JOIN `groups` ON students.group_id = `groups`.id
WHERE students.id = %s
"""
cursor.execute(sql_select_student, (student_id,))
student_info = cursor.fetchone()
print(f"Студент {student_info[0]} {student_info[1]} находится в группе '{student_info[2]}'")

# Запрос INSERT для subjects
sql_subjects = (
    "INSERT INTO subjets (title) "
    "VALUES (%s), (%s)"
)
cursor.execute(sql_subjects, ('Python cours', 'SQL cours'))
subject_ids = cursor.lastrowid  # Получаем id добавленных записей

# Запрос INSERT для lessons
sql_lessons = (
    "INSERT INTO lessons (title, subject_id) "
    "VALUES (%s, %s), (%s, %s)"
)
cursor.execute(sql_lessons, ('Lesson 10', subject_ids, 'Lesson 20', subject_ids + 1))
lesson_ids = cursor.lastrowid  # Получаем id добавленных записей

# Запрос INSERT для marks
sql_marks = (
    "INSERT INTO marks (value, lesson_id, student_id) "
    "VALUES (%s, %s, %s), (%s, %s, %s)"
)
cursor.execute(sql_marks, (10, lesson_ids, student_id, 'good', lesson_ids + 1, student_id))

# Запросы SELECT для вывода информации
sql_select_marks = (
    "SELECT m.value, l.title AS lesson_title "
    "FROM marks m JOIN lessons l ON m.lesson_id = l.id "
    "WHERE m.student_id = %s"
)
cursor.execute(sql_select_marks, (student_id,))
marks_info = cursor.fetchall()
print("Оценки студента:")
for mark in marks_info:
    print(f"{mark[1]}: {mark[0]}")

sql_select_books = "SELECT b.title FROM books b WHERE b.taken_by_student_id = %s"
cursor.execute(sql_select_books, (student_id,))
books_info = cursor.fetchall()
print("Книги, взятые студентом:")
for book in books_info:
    print(book[0])

sql_select_student_details = """
SELECT
    students.id,
    students.name,
    students.second_name,
    `groups`.title AS group_title,
    `groups`.start_date,
    `groups`.end_date,
    GROUP_CONCAT(DISTINCT books.title) AS books,
    GROUP_CONCAT(DISTINCT subjets.title) AS subjects,
    GROUP_CONCAT(DISTINCT lessons.title) AS lessons,
    GROUP_CONCAT(DISTINCT marks.value) AS marks
FROM
    students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN books ON students.id = books.taken_by_student_id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
WHERE
    students.id = %s
GROUP BY
    students.id, students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date
"""
cursor.execute(sql_select_student_details, (student_id,))
student_details = cursor.fetchone()
print(
    f"\nИнформация о студенте:\n"
    f"ID: {student_details[0]}\n"
    f"Имя: {student_details[1]}\n"
    f"Фамилия: {student_details[2]}\n"
    f"Группа: {student_details[3]}\n"
    f"Дата начала группы: {student_details[4]}\n"
    f"Дата окончания группы: {student_details[5]}\n"
    f"Книги: {student_details[6]}\n"
    f"Предметы: {student_details[7]}\n"
    f"Уроки: {student_details[8]}\n"
    f"Оценки: {student_details[9]}"
)

# Подтверждение изменений в базе данных
db.commit()

# Закрытие курсора и соединения с базой данных
cursor.close()
db.close()
