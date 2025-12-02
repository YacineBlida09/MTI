#Write in procedural and functional programming the N'th triangular number.> (1+2+3+...+n)

n = 5
#Procedural
def triangular(n):
    if n == 1:
        return 1
    elif n > 1:
        return n + triangular(n-1)
    else: 
        return None

print("Procedural: nth triangular de 5 est "+str(triangular(n)))

#Functional
from functools import reduce

res = reduce(lambda x,y : x + y, range(1, n + 1))

print("Functional: nth triangular de 5 est "+str(triangular(n)))