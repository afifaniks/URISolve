t = input()

a = list(map(str, input().split()))


booli = True
kooli = False

fir = int(a[0])
sec = int(a[1])

if fir>sec:
    kooli = True
    
x=len(a)

up = a[0]

if kooli:
    l = 1

    while l<len(a):
        up = a[l]
        if l%2==0:
            if int(a[l])<=int(a[l-1]):
                booli = False
                break
        else:
            if int(a[l])>=int(a[l-1]):
                booli = False
                break
        l+=1
        
else:
    l = 1
    while l<len(a):
        up = a[l]
        if l%2==0:
            if int(a[l])>=int(a[l-1]):
                booli = False
                break
        else:
            if int(a[l])<=int(a[l-1]):
                booli = False
                break
        l+=1
    
            
if booli:
    print("1")
else:
    print("0")
