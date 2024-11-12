numeros=[2,4,1,45,75,22]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

usuarios=[[4, "Chanchito"], [1, "Felipe"], [2, "Bodin"]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=False)
print(usuarios)

usuarios.sort(key=lambda el:el[1])
print(usuarios)