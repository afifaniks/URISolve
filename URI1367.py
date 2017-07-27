a = int(input())

while a!=0:
    arr = list()
    brr = list()
    crr = list()

    point = 0
    no = 0
    
    for i in range(0,a):
        j, k, l = input().split()

        arr.append(j)
        brr.append(k)
        crr.append(l)

        if l == "correct":
            cnt = arr.count(j)

            if cnt>=1:
                cnt-=1

            point+=(int(k)+(cnt*20))
            no+=1

    print(str(no)+" "+str(point))

    a = int(input())
