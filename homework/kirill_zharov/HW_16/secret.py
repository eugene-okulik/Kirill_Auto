import mysql.connector as mysql
import cred
import os
import dotenv
import csv

dotenv.load_dotenv()
# Подключение к базе данных
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
# print(homework_path)
# Построение пути к файлу конфигурации относительно текущего файла
config_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")
#print(config_path)

with open(config_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_data = [row for row in csv_reader]

csv_data_tuples = [tuple(row) for row in csv_data]

#print(csv_data_tuples)

# Создание объекта для выполнения SQL-запросов
cursor = db.cursor(dictionary=True)
cursor.execute("""
SELECT *
FROM students;
""")
data = cursor.fetchall()
db_data_tuples = [tuple(row) for row in data]
#print(db_data_tuples)

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

