class Author:
    def __init__(self, name: str, country: str, birth_date: str):
        self.name = name
        self.country = country
        self.birth_date = birth_date
        self.books = []

    def __str__(self):
        return f"{self.name} ({self.birth_date}) from {self.country}"

    def __repr__(self):
        return f"Author('{self.name}', '{self.country}', '{self.birth_date}')"


class Book:
    total_books = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __str__(self):
        return f"'{self.name}' by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.name}', {self.year}, {self.author})"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return f"{self.name} library with {len(self.books)} books by {len(self.authors)} authors"

    def __repr__(self):
        return f"Library('{self.name}')"


author1 = Author("Jane Austen", "England", "16 December 1775")

library = Library("Central Library")

library.new_book("Pride and Prejudice", 1813, author1)

library.new_book("Emma", 1815, author1)

print(f"Books by {author1}: {library.group_by_author(author1)}")

print(f"Books from 1813: {library.group_by_year(1813)}")
