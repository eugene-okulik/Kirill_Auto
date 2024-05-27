import sys

# Устанавливаем лимит на количество символов в строковом представлении целых чисел
sys.set_int_max_str_digits(100000)

def fibonacci_generator():
    """Генератор чисел Фибоначчи."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci_number_at_index(index):
    """Возвращает число Фибоначчи по заданному индексу."""
    fib_gen = fibonacci_generator()
    for _ in range(index):
        number = next(fib_gen)
    return number

# Получаем числа Фибоначчи для указанных индексов
indices = [5, 200, 1000, 100000]
for index in indices:
    print(f"{index}-е число Фибоначчи: {get_fibonacci_number_at_index(index - 1)}")
