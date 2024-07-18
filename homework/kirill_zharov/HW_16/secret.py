import os
import csv
import dotenv
import mysql.connector as mysql

# Загрузка переменных окружения из .env файла
dotenv.load_dotenv()

# Подключение к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

# Получаем базовый путь к директории, в которой находится текущий файл скрипта
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))

# Построение пути к файлу конфигурации относительно текущего файла
config_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

# Чтение данных из CSV файла
with open(config_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_data = [row for row in csv_reader]

csv_data_tuples = [tuple(row) for row in csv_data]

# Создание объекта для выполнения SQL-запросов
cursor = db.cursor(dictionary=True)
cursor.execute("""
    SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title,
           sub.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
    FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON b.taken_by_student_id = s.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets sub ON l.subject_id = sub.id
""")
data = cursor.fetchall()

db_data_tuples = [(
    row['name'],
    row['second_name'],
    row['group_title'],
    row['book_title'],
    row['subject_title'],
    row['lesson_title'],
    row['mark_value']
) for row in data]

# Поиск отсутствующих данных
missing_data = [row for row in csv_data_tuples if row not in db_data_tuples]

if missing_data:
    print("Этих данных нет в базе:")
    for row in missing_data:
        print(row)
else:
    print("Все данные из файла есть в базе.")

# Закрытие соединения с базой данных
cursor.close()
db.close()
