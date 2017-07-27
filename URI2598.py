import math

a = int(input())

for i in range(0,a):
    x, y = input().split()

    x = int(x)
    y = int(y)

    gg = x/y

    print(math.ceil(gg))

