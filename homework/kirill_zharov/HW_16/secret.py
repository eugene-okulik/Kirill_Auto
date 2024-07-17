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
SELECT *
FROM students;
""")
data = cursor.fetchall()
db_data_tuples = [tuple(row.values()) for row in data]

# Поиск отсутствующих данных
missing_data = [row for row in csv_data_tuples if row not in db_data_tuples]

if missing_data:
    print("Этих данных не хватает в базе:")
    for row in missing_data:
        print(row)
else:
    print("Все данные из файла присутствуют в базе.")

# Закрытие соединения с базой данных
cursor.close()
db.close()
