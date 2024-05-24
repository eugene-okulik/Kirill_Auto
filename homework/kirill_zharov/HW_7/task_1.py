while True:
    number = 10
    user = int(input("Введите любое число oт 1 до 10:"))
    if user == number:
        print("Поздравляю! Вы угадали!")
        break
    elif user != number:
        print("Попробуйте снова")

print("Good bye")
