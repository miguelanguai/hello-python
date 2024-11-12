usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

nombres = [usuario[0] for usuario in usuarios]
print(nombres)

#filtrar
nombres = [usuario for usuario in usuarios if usuario[1]>2]
print(nombres)

#filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1]>2]
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1]>2, usuarios))
print(menosUsuarios)