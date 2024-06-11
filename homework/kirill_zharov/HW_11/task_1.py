class Book:
    material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        self.reserved = True

    def __str__(self):
        reservation_status = "зарезервирована" if self.reserved else "не зарезервирована"
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                f"материал: {Book.material}, {reservation_status}")


book1 = Book("Идиот", "Достоевский", 400, "123456712")
book2 = Book("Три товарища", "Ремарк", 250, "234567878")
book3 = Book("Старик и море", "Хемингуэй", 300, "3456789045")
book4 = Book("Финансист", "Драйзер", 500, "45678906434")
book5 = Book("Принцесса на горошине", "Андерсен", 15, "5678341234")

book1.reserve()

books = [book1, book2, book3, book4, book5]
for book in books:
    print(book)


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, subject, school_class, has_exercises):
        super().__init__(title, author, pages, isbn)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

    def __str__(self):
        reserved_status = 'зарезервирована' if self.reserved else 'не зарезервирована'
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
                f"предмет: {self.subject}, класс: {self.school_class}, {reserved_status}".strip())


textbooks = [
    Textbook("Алгебра", "Жаров", 200, "978-0-00-744327-4", "Математика", 9, True),
    Textbook("Биология", "Петров", 300, "978-0-00-748326-3", "Биология", 11, False),
    Textbook("География", "Уткин", 250, "978-0-00-741409-0", "География", 8, True),
    Textbook("Физика", "Лебедев", 400, "978-0-00-744329-8", "Физика", 10, True),
    Textbook("Химия", "Боранов", 320, "978-0-00-744320-5", "Химия", 9, False)
]

textbooks[2].reserve()

for textbook in textbooks:
    print(textbook)
