#●​ Classes: Book, Member, Librarian, Library
# ●​ A member can borrow and return books.
# ●​ A librarian can add or remove books.
# ●​ Track borrowed books and display available ones.
# ●​ Exception handling for unavailable books.
# ●​ Abstract Person class for Member and Librarian.
# ●​ Use of private attributes and getter/setter methods.

class Library:
    __code = 1
    __available_books = []
    __taken_books = []
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__code = Library.__code
        Library.__code += 1

    def take_from(self, book):
        self.__available_books.remove(book)
        self.__taken_books.append(book)
    
    def add_book(self, book):
        self.__available_books.append(book)
    
    def remove_book(self, book):
        self.__available_books.remove(book)

    def __str__(self):
        return f"Library number {self.__code:04d} contains these books " + "\n".join(map(str, self.__available_books)) + "\nwhile these are taken" + "\n".join(map(str, self.__taken_books))


class Book:
    __code = 1
    __title, __author, __taken = "", "", 0
    def __init__(self, title, author):
        self.__code = Book.__code
        Book.__code += 1
        self.__title = title
        self.__author = author

    def set_taken(self, state):
        self.__taken = state

    def istaken(self):
        return self.__taken == 1

    def __str__(self):
        return f"\tCode: {self.__code:04d}\n\tTitle: {self.__title}\n\tAuthor: {self.__author}"

class Member:
    __code = 1
    def __init__(self, name):
        self.__code = Member.__code
        Member.__code += 1
        self.__name = name
        self.__books = [] 

    def borrow(self, book):
        if book.istaken():
            print(f"unfortunately \n{book}\nis already taken.")
        else: 
            book.set_taken(1)
            self.__books.append(book)
            

    def give_back(self, book):
        book.set_taken(0)
        self.__books.remove(book)

    def __str__(self):
        return f"Member: \n\tCode: {self.__code:04d}\n\tName: {self.__name}\n\tBooks:\n " + "\n".join(map(str, self.__books))
    
class Librarian:
    __code = 1
    def __init__(self,name):
        self.__name = name
        self.__code = Librarian.__code
        Librarian.__code += 1
    
    def add_book_to_library(self, book, library):
        library.add_book(book)
    
    def remove_book_from_library(self, book, library):
        library.remove_book(book)
    
    def __str__(self):
        return f"Librarian: \n Code: {self.__code}, Name: {self.__name}"


#b1 = Book("Iron Man Manual", "pdiddy")
#b2 = Book("Hulk Smash", "epstein")
#m1 = Member("Stark")
#m1.borrow(b1)
#print(m1)
#m2 = Member("Banner")
#m2.borrow(b2)
#print(m2)
#m2.borrow(b1)
#m1.give_back(b1)
#print(m1)
#m2.borrow(b1)
#print(m2)

l1 = Librarian("Behzinga")
print(l1)
l2 = Librarian("Sidawg")
print(l2)
lib = Library("Sidemen", "UK")
print(lib)
b1 = Book("Iron Man Manual", "pdiddy")
print(b1)
b2 = Book("Hulk Smash", "epstein")
print(b2)
l1.add_book_to_library(b1, lib)
l2.add_book_to_library(b2, lib)
l2.add_book_to_library(b2, lib)
print(lib)
l2.remove_book_from_library(b2,lib)
print(lib)

