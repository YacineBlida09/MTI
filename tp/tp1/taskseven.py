#Find the first prime number greater than 100 using a loop and break.
i = 100 
while True:
    i += 1
    for j in range(2, int(i**.5)+1):
        if i % j == 0: 
            break
    else : #else de for (si for didnt break)
        print(f"le 1er nbr premier apres 100 est: {i}")
        break

#Print all numbers from 1 to 20, except for multiples of 3, using continue.

for i in range(1, 21):
    if i % 3 == 0:
        continue
    else:
        print(str(i))