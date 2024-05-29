from datetime import datetime


date = "Jan 15, 2023 - 12:05:33"

date_obj = datetime.strptime(date, "%b %d, %Y - %H:%M:%S")


print(date_obj.strftime("%B"))
print(f"{date_obj:%d.%m.%Y, %H:%M}")
