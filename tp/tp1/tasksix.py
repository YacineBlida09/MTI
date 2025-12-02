#Receive integers from the user until he enter 0, then calculate and print the average of the entered numbers (excluding 0).
somme, i, entier = 0, 0, None
while entier != 0:
    entier = int(input("Donner un entier different de 0:\t"))
    if entier != 0:
        i += 1
    somme += entier

print(f"la Moyenne est: {somme/i}")

#Use a do-while loop to repeatedly ask the user for a number until he enter a positive value. If the user reads a positive number, we leave the loop and display a message confirming the read of a positive value.
while True:
     entier = int(input("Donner un entier positif pour arreter le program:\t"))
     if entier > 0 :
        print("cbon")
        break
