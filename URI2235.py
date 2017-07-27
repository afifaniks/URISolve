a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

booli = False

if a==b:
    booli = True

elif a==c:
    booli = True

elif b==c:
    booli = True

elif a>b and a>c and (b+c)==a:
    booli = True

elif b>a and b>c and (a+c)==b:
    booli = True

elif c>b and c>a and (a+b)==c:
    booli = True


if booli:
    print("S")

else:
    print("N")
