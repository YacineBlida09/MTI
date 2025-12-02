#1. Implement a basic calculator that performs addition, subtraction, multiplication, and division.
# 2. Break down the calculator into functions, ensuring procedural flow.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None
    return a / b

a, b = input("Entrez deux nombres separes par une virgule: ").split(',')
a = float(a)
b = float(b)

choix = ''
while choix != '+' and choix != '-' and choix != '*' and choix != '/':
    choix = input("Choisissez une operation (+, -, *, /): ")
    match choix:
        case "+":
            res = add(a, b)
        case "-":
            res = sub(a, b)
        case "*":
            res = mul(a, b)
        case "/":
            res = div(a, b)
        case _:
            print("Operation non reconnue, veuillez reessayer.")

if res is not None:
    print(f"Le resultat de l'operation est: {res}")
else:
    print("Erreur: Division par zero.")