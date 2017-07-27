ctr = 0

a, b = input().split()

a = int(a)
b = int(b)

ctr+=a

for i in range(0,b):
    x = input()

    if x == "fechou":
        ctr+=1
    elif x == "clicou":
        ctr-=1

print(ctr)
