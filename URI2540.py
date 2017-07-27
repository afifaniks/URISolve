while True:
    try:
        a = input()

        arr = list(map(str, input().split()))

        strlen = len(arr)

        on = arr.count("1")

        if on>=((2/3)*strlen):
            print("impeachment")
        else:
            print("acusacao arquivada")

    except EOFError:
        break

