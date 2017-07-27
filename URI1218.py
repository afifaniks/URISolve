x=1
while True:
    try:           
        a = input()
        arr = list(map(str, input().split()))

        i = 0
        m = 0
        f = 0

        while i<len(arr):
            if arr[i]==a and arr[i+1]=="M":
                m+=1
            elif arr[i]==a and arr[i+1]=="F":
                f+=1
            i+=1
            
        if x!=1:
            print()
        
        print("Caso "+str(x)+":\nPares Iguais: "+str(m+f)+"\nF: "+str(f)+"\nM: "+str(m))
        x+=1

    except EOFError:
        break
