import random

while True:
    salary = int(input("Введите вашу зарплату: "))
    bonus = random.choice([True, False])

    if bonus:
        salary += random.randint(1, 5000)

    print(f"${salary}")
