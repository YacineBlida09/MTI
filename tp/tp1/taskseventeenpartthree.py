library = {
"The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925}, 
"1984": {"author": "George Orwell", "year": 1949}
}

#Access and print the author of "1984".
for book in library:
    if book == "1984":
        print(library[book]["author"])

#Add a new book: "To Kill a Mockingbird", by "Harper Lee", published in 1960.
library["To Kill a Mockingbird"] = {"author": "Harper Lee", "year": 1960}
print(library)

#Print all book titles and their respective authors
for book in library:
    print(f"Titre: {book} Auteur: {library[book]["author"]}")