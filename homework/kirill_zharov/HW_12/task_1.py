class Flower:
    def __init__(self, name, color, stem_length, freshness, lifespan, cost):
        """Инициализация класса Flower."""
        self.name = name
        self.color = color
        self.stem_length = stem_length  # длина стебля в см
        self.freshness = freshness  # свежесть в днях
        self.lifespan = lifespan  # среднее время жизни в днях
        self.cost = cost  # стоимость цветка в рублях

    def __str__(self):
        """Возвращает строковое представление цветка."""
        return (f"{self.name} ({self.color}), длина стебля: {self.stem_length} см, "
                f"свежесть: {self.freshness} дней, стоимость: {self.cost} руб.")


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, lifespan, cost):
        """Инициализация класса Rose."""
        super().__init__("Роза", color, stem_length, freshness, lifespan, cost)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, lifespan, cost):
        """Инициализация класса Tulip."""
        super().__init__("Тюльпан", color, stem_length, freshness, lifespan, cost)


class Daisy(Flower):
    def __init__(self, color, stem_length, freshness, lifespan, cost):
        """Инициализация класса Daisy."""
        super().__init__("Ромашка", color, stem_length, freshness, lifespan, cost)


class Bouquet:
    def __init__(self):
        """Инициализация класса Bouquet."""
        self.flowers = []

    def add_flower(self, flower):
        """Добавляет цветок в букет."""
        self.flowers.append(flower)

    def calculate_cost(self):
        """Вычисляет общую стоимость букета."""
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        """Вычисляет среднее время жизни цветов в букете."""
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        """Сортирует цветы в букете по заданному ключу."""
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers_by_lifespan(self, lifespan):
        """Ищет цветы в букете по заданному времени жизни."""
        return [flower for flower in self.flowers if flower.lifespan == lifespan]

    def __str__(self):
        """Возвращает строковое представление букета."""
        return "\n".join(str(flower) for flower in self.flowers)


# Создаем экземпляры цветов
rose1 = Rose("красный", 50, 5, 7, 150)
rose2 = Rose("белый", 45, 4, 6, 140)
tulip1 = Tulip("желтый", 30, 3, 5, 100)
daisy1 = Daisy("белый", 20, 2, 10, 80)
daisy2 = Daisy("розовый", 25, 2, 10, 90)

# Создаем букет и добавляем цветы
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(daisy1)
bouquet.add_flower(daisy2)

# Печатаем детали букета
print("Букет:")
print(bouquet)
print(f"\nСтоимость букета: {bouquet.calculate_cost()} руб.")
print(f"Среднее время жизни букета: {bouquet.average_lifespan()} дней")

# Сортируем цветы в букете по длине стебля и печатаем
bouquet.sort_flowers("stem_length")
print("\nБукет после сортировки по длине стебля:")
print(bouquet)

# Поиск цветов по среднему времени жизни и печать
found_flowers = bouquet.find_flowers_by_lifespan(10)
print("\nЦветы с временем жизни 10 дней:")
for flower in found_flowers:
    print(flower)
