while True:
    try:
        a = int(input())
        gg = 0.0
        kk = 0.0
            
        for i in range(0,a):
            x, y = input().split()

            x = int(x)
            y = int(y)

            gg+=(x*y)
            kk+=(y*100)

        print("%0.4f"%(gg/kk))


    except EOFError:
        break
