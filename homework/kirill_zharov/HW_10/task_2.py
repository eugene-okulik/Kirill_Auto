def repeat(func):
    def wrapper(*args, count=1, **kwargs):
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat
def example(text):
    print(text)


example('print me', count=2)
