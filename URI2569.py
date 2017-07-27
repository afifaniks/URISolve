a, b, c = input().split()

for i in a:
    if i=="7":
        a = a.replace(i,"0")

for i in c:
    if i=="7":
        c = c.replace(i,"0")

if b=="+":
    g=str(int(a)+int(c))
elif b=="x":
    g=str(int(a)*int(c))

for i in g:
    if i=="7":
        g = g.replace(i,"0")

g = int(g)

print(g)
