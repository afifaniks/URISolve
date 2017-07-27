t = int(input())

for loop in range(0,t):
    a = int(input())
    arr = list()
    brr = list()

    arr = list(map(str, input().split()))
    brr = list(map(str, input().split()))

    sss = True
    x=0

    for i in brr:
        su=0
        mm=0
        for c in i:
            if c=="P":
                su+=1
            if c=="M":
                mm+=1

        lens = int(len(i))-mm

        if float(su)<float(lens*0.75):
            if sss:
                print(arr[x],end="")
                sss = False
            else:
                print(" "+arr[x],end="")
        x+=1

    print()
