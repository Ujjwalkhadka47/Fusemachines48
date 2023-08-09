
#The Book class is responsible for representing the book attributes and its availability status, while the
#LibraryCatalog class is responsible for managing the collection of books and handling borrowing and returning processes

#Single-Responsibility Principle (SRP)

class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.is_available = True

    def get_details(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Status: {availability}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_details(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.get_details()
        return "Book not found in the catalog."

    def get_all_books(self):
        return [book.get_details() for book in self.books]

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    return f"Successfully borrowed the book: {book.title}"
                else:
                    return "Book is not available for borrowing."
        return "Book not found in the catalog."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.is_available = True
                    return f"Successfully returned the book: {book.title}"
                else:
                    return "Book is already available for borrowing."
        return "Book not found in the catalog."


# Testing the classes
if __name__ == "__main__":
    catalog = LibraryCatalog()

    # Adding books to the catalog
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction")
    book3 = Book("1984", "George Orwell", "9780451524935", "Science Fiction")

    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    # Display all books in the catalog
    print("All Books in the Catalog:")
    for book_details in catalog.get_all_books():
        print(book_details)

    # Borrowing a book
    isbn_to_borrow = "9780316769488"
    print(catalog.borrow_book(isbn_to_borrow))

    # Display book details after borrowing
    print("\nBook Details after Borrowing:")
    for book_details in catalog.get_all_books():
        print(book_details)

    # Returning a book
    isbn_to_return = "9780316769488"
    print(catalog.return_book(isbn_to_return))

    # Display book details after returning
    print("\nBook Details after Returning:")
    for book_details in catalog.get_all_books():
        print(book_details)









    