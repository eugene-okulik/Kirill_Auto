import os
from datetime import datetime, timedelta

# Получаем базовый путь к директории, в которой находится текущий файл скрипта
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
print(homework_path)
# Построение пути к файлу конфигурации относительно текущего файла
config_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")
print(config_path)
# Открываем файл конфигурации и читаем его содержимое
with open(config_path, 'r') as config_file:
    config_data = config_file.read()
    print(config_data)

# Задача 1: Прибавить одну неделю к дате 2023-11-27 20:34:13.212967
orig_date = datetime.strptime('2023-11-27 20:34:13.212967', '%Y-%m-%d %H:%M:%S.%f')
new_date = orig_date + timedelta(weeks=1)
print(f"Дата {orig_date} + 1 неделя = {new_date}")

# Задача 2: Определить день недели для даты 2023-07-15 18:25:10.121473
date_str_2 = '2023-07-15 18:25:10.121473'
date_obj_2 = datetime.strptime(date_str_2, '%Y-%m-%d %H:%M:%S.%f')
day_of_week = date_obj_2.strftime('%A')
print(f"{date_str_2} - это {day_of_week}")

# Задача 3: Вычислить количество дней с даты 2023-06-12 15:23:45.312167 до текущей даты
date_str_3 = '2023-06-12 15:23:45.312167'
date_obj_3 = datetime.strptime(date_str_3, '%Y-%m-%d %H:%M:%S.%f')
current_date = datetime.now()
difference = current_date - date_obj_3
days_difference = difference.days
print(f"{date_str_3} была {days_difference} дней назад")
