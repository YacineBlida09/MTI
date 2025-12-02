# File: python/test.py
# python/test.py

def add(a, b):
    return a + b

stop = ''

while stop.lower() != 'q':
    while True:
        try:
            n1, n2 = input("Give me two numbers separated by space: ").split()
            n1, n2 = float(n1), float(n2)
            break 
        except ValueError:
            print("Invalid input. Please enter two numbers.")

    print("Your result:", add(n1, n2))

    stop = input("\nIf you'd like to stop, enter 'q' for quit. Otherwise, press Enter: ")
