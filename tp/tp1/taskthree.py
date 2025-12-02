#Write a program that checks if a number is positive, negative, or zero.
n = int(input("Donner un entier\n"))
if n > 0:
    print(f"{n} est positif")
elif n < 0: 
    print(f"{n} est negatif")
else:
    print(f"{n} est nul")

#Create a program that determines if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400
n = int(input("Donner une annee\n"))
if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0): 
    print("29j")
else:
    print("28j")
