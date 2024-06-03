def operation_selector(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@operation_selector
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        raise ValueError("Invalid operation")


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

result = calc(first, second)

print(f"Результат: {result}")
