a = input()

b = list(map(str, input().split()))

k=0

for i in b:
    if len(i)==3 and i[0]=="O" and i[1]=="B":
        if k==0:
            print("OBI", end="")
            k+=1
        else:
            print(" OBI", end="")
            k+=1

    elif len(i)==3 and i[0]=="U" and i[1]=="R":
        if k==0:
            print("URI", end="")
            k+=1
        else:
            print(" URI", end="")
            k+=1
            

    else:
        if k==0:
            print(i, end="")
            k+=1
        else:
            print(" "+i,end="")
            k+=1
print()

