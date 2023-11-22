class Author:
    def __init__(self, author_name):
        self.author_name = author_name

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def checkout(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return f"Book '{self.title}' checked out successfully."
        else:
            return f"Sorry, '{self.title}' is currently unavailable."

    def checkin(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return f"Book '{self.title}' checked in successfully."
        else:
            return f"All copies of '{self.title}' are already available."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author_name, total_copies):
        author = Author(author_name)
        book = Book(title, author, total_copies)
        self.books.append(book)
        return f"Book '{title}' added to the library."

    def search_by_author(self, author_name):
        found_books = [book.title for book in self.books if book.author.author_name == author_name]
        if found_books:
            return found_books
        else:
            return f"No books found for author '{author_name}'."

    def search_by_title(self, title):
        found_books = [book.title for book in self.books if book.title == title]
        if found_books:
            return found_books
        else:
            return f"No books found with title '{title}'."


library = Library()
print(library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5))
print(library.add_book("To Kill a Mockingbird", "Harper Lee", 3))
print(library.search_by_author("F. Scott Fitzgerald"))
print(library.search_by_title("To Kill a Mockingbird"))


gatsby_book = library.books[0]
print(gatsby_book.checkout())
print(gatsby_book.checkin())
