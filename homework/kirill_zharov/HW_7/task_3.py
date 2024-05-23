def some_func(results):


    for text in results:
        number = int(text.split()[-1]) + 10
        print(number)

results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

some_func(results)
