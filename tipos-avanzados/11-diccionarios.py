punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])

punto["z"]=45
print(punto)

if "lala" in punto:
    print(punto, punto["lala"])


print(punto.get("x"))
print(punto.get("lala", 97)) #si no existe, saca 97

del punto["x"]
del(punto["y"])
print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)
    
for llave, valor in punto.items():
    print(llave, valor)
    
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Pepe"},
]

for usuario in usuarios:
    print(usuario["nombre"])
