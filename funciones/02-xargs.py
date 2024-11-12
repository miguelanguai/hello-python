def suma(*numeros):
    print(numeros)
    res = 0
    for n in numeros:
        res +=n
    print(res)

suma(2,5)
suma(1,2,3,4,5)