while True:
    try:
        a = int(input())
        arr = list()

        for i in range(0,a):
            arr.append(input())

        arr = sorted(arr)

        for i in range(0,a):
            print(arr[i])

    except EOFError:
        break
