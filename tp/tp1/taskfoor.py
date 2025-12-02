#Implement a simple grading system: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
note = int(input("Donner votre note sur 100:\n"))
if note > 100 or note < 0:
    print("note saisie incorrecte")
elif note < 60:
    print("F")
elif note < 70:
    print("D")
elif note < 80:
    print("C")
elif note < 90:
    print("B")
else:
    print("A")

#Write a program that takes a day number (1-7) and prints the corresponding day name (e.g., 1 for Saturday, 2 for Sunday)
jour = int(input("Donner un nombre [1-7]\n"))
match jour:
    case 1:
        print("Dimanche")
    case 2:
        print("Lundi")
    case 3:
        print("Mardi")
    case 4:
        print("Mercredi")
    case 5:
        print("Jeudi")
    case 6:
        print("Vendredi")
    case 7:
        print("Samedi")
    case _:
        print("Erreure de saisie")