#1. Implement a program that processes a list of numbers, applying map, filter, and reduce operations.
# 2. Use lambda functions to create a concise, functional style.

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

map_res = list(map(lambda x: x**.5, numeros))

for n in map_res:
    print(f"racine de {round(n**2)} est: {n:.2f} ")

filt_res = list(filter(lambda x: x % 2 == 0, numeros))
print(filt_res)

reduce_res = reduce(lambda x, y: x ** y, numeros)
print(reduce_res)