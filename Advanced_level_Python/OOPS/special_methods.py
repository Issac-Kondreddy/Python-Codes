class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.pages})"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

# Using the special methods
book1 = Book("Python Programming", "Jane Doe", 300)
book2 = Book("Advanced Python", "John Smith", 450)

print(book1)  # Calls __str__
print(repr(book1))  # Calls __repr__
print(len(book1))  # Calls __len__
print(book1 + book2)  # Calls __add__, summing up the pages of both books
