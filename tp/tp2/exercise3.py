#Create a simple "Library System" with classes for `Book`, `Author`, and `Library`.

class Author:
    def __init__(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance

    def get_author_info(self):
        return f"{self.nom} (né en {self.annee_naissance})"

    def set_author_info(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance

class Book:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def get_book_info(self):
        return f"'{self.titre}' par {self.auteur.get_author_info()} (publié en {self.annee_publication})"

    def set_book_info(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Library:
    books = []
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_book_info())

#Implement inheritance (e.g., `EBook` as a subclass of `Book`) and use polymorphism (e.g., method
class EBook(Book):
    def __init__(self, titre, auteur, annee_publication, taille_fichier):
        super().__init__(titre, auteur, annee_publication)
        self.taille_fichier = taille_fichier

    def get_book_info(self):
        return f"'{self.titre}' par {self.auteur.get_author_info()} (publié en {self.annee_publication}, taille du fichier: {self.taille_fichier}MB)"
