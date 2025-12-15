# File: python/prdivfast.py
import math

def prdiv(n):
    if n < 2:
        return []
    
    divT = []
    temp_n = n
    
    # Handle 2 separately
    power = 0
    while temp_n % 2 == 0:
        temp_n //= 2
        power += 1
    if power > 0:
        divT.append({"prime": 2, "power": power})
    
    # Check odd factors only, up to sqrt(n)
    factor = 3
    while factor * factor <= temp_n:
        power = 0
        while temp_n % factor == 0:
            temp_n //= factor
            power += 1
        if power > 0:
            divT.append({"prime": factor, "power": power})
        factor += 2
    
    # If what remains is greater than 1, it's prime
    if temp_n > 1:
        divT.append({"prime": temp_n, "power": 1})
    
    return divT

stop = ''

while stop.lower() != 'q':
    while True:
        try:
            usrin = input("Give me a number: ")
            usrin = int(usrin)
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Your result:")
    res = prdiv(usrin)
    if not res:
        print("No prime factors found (the number might be 0, 1, or negative).")
    else:
        output = ""
        for factor in res:
            output += f"{factor['prime']}^{factor['power']} × "
        output = output.rstrip(" × ") 
        print(output)

    stop = input("\nIf you'd like to stop, enter 'q' for quit. Otherwise, press Enter: ")