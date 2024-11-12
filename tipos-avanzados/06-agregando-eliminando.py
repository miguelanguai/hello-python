mascotas=[
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe"
    "Pulga",
    "Chanchito feliz"
]
mascotas.insert(1,"Melvin")
mascotas.append("Chanchito triste")

mascotas.remove("Pulga") #elimina el primero
mascotas.pop()
mascotas.pop(1) #elimina el uno
del mascotas[0]
mascotas.clear()
print(mascotas)