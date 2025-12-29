from library.book import Book
from library.storage import load_books, save_books


class LibraryManager:
    def __init__(self):
        self.books = load_books()

    def add_book(self, title, author, year):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author, year)
        self.books.append(book.to_dict())
        save_books(self.books)
        return book

    def list_books(self):
        return self.books

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b["title"].lower()]

    def remove_by_id(self, book_id):
        self.books = [b for b in self.books if b["id"] != book_id]
        save_books(self.books)
