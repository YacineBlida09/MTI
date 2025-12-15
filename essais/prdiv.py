# File: python/prdiv.py
def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: 
            return False
    return True        

def prdiv(n):
    if n < 2:
        return []
    
    divT = []
    temp_n = n
    
    # Check for factor 2 separately to handle even numbers efficiently
    if temp_n % 2 == 0:
        power = 0
        while temp_n % 2 == 0:
            temp_n = temp_n // 2
            power += 1
        divT.append({"prime": 2, "power": power})
    
    # Check odd factors only
    for i in range(3, n // 2 + 1, 2):
        if isprime(i) and temp_n % i == 0:
            power = 0
            while temp_n % i == 0:
                temp_n = temp_n // i
                power += 1
            divT.append({"prime": i, "power": power})
    
    # If n itself is prime
    if not divT and n >= 2:
        divT.append({"prime": n, "power": 1})
    
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