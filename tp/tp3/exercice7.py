#●​ Classes: Book, Member, Librarian, Library
# ●​ A member can borrow and return books.
# ●​ A librarian can add or remove books.
# ●​ Track borrowed books and display available ones.
# ●​ Exception handling for unavailable books.
# ●​ Abstract Person class for Member and Librarian.
# ●​ Use of private attributes and getter/setter methods.

class Book:
    __title = ""
    __author = ""
    __editor = ""
    __date = ""
    def __init__(self, title, author, editor, date):
        self.__title = title
        self.__author = author
        self.__editor = editor
        self.__date = date

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_editor(self):
        return self.__editor

    def get_date(self):
        return self.__date

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_editor(self, editor):
        self.__editor = editor

    def set_date(self, date):
        self.__date = date
    
    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Editor: {self.__editor}, Date: {self.__date}"
    
class Member:
    __name = ""
    __code = ""
    __borrowed_books = []
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book, library):
        library.lend_book(book, self)

    def return_book(self, book, library):
        library.receive_book(book, self)

    def add_borrowed_book(self, book):
        self.__borrowed_books.append(book)

    def remove_borrowed_book(self, book):
        self.__borrowed_books.remove(book)

    def list_borrowed_books(self):
        return [str(book) for book in self.__borrowed_books]

class Librarian:
    __name = ""
    __employee_id = ""
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def add_book(self, book, library):
        library.add_book(book)

    def remove_book(self, book, library):
        library.remove_book(book)

class Library:
    __books = []
    __borrowed_books = {}
    def __init__(self):
        pass

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            raise Exception("Book not found in library.")

    def lend_book(self, book, member):
        if book in self.__books:
            self.__books.remove(book)
            self.__borrowed_books[book] = member
            member.add_borrowed_book(book)
        else:
            raise Exception("Book is not available for borrowing.")

    def receive_book(self, book, member):
        if book in self.__borrowed_books and self.__borrowed_books[book] == member:
            self.__books.append(book)
            del self.__borrowed_books[book]
            member.remove_borrowed_book(book)
        else:
            raise Exception("This book was not borrowed by this member.")

    def list_available_books(self):
        return [str(book) for book in self.__books]

    def list_borrowed_books(self):
        return {str(book): member.get_name() for book, member in self.__borrowed_books.items()}

if __name__ == "__main__":
    library = Library()
    librarian = Librarian("Alice", "L001")
    member = Member("Bob", "M001")

    book1 = Book("1984", "George Orwell", "Secker & Warburg", "1949")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "1960")

    librarian.add_book(book1, library)
    librarian.add_book(book2, library)

    print("Available books:", library.list_available_books())

    member.borrow_book(book1, library)
    print("Available books after borrowing:", library.list_available_books())
    print("Bob's borrowed books:", member.list_borrowed_books())

    member.return_book(book1, library)
    print("Available books after returning:", library.list_available_books())
    print("Bob's borrowed books after returning:", member.list_borrowed_books())
