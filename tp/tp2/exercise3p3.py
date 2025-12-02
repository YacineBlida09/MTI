#Recursive Fibonacci Sequence
# Write in procedural and functional programming the Fibonacci number. Run the program for n=6.(n-2 + n-1 + n)

n = 6
#Procedural
def fib(n):
    if n == 0 or n == 1:
        return 1
    elif n >= 2:
        return (fib(n - 1) + fib(n - 2))
    else:
        return None

print("Procedural: fib de 6 est "+str(fib(6)))

#Functional 
from functools import reduce

res = reduce(lambda t, _: (t[1], t[0] + t[1]), range(n - 1), (1, 1))[0]

print("Functional: fib de 6 est "+str(fib(6)))