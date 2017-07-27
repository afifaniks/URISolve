import math
a = int(input())

while a!=0:
    ger = math.ceil(7*a/90)
    bra = math.floor(a/90)

    print("Brasil "+str(bra)+" x Alemanha "+str(ger))

    a = int(input())
