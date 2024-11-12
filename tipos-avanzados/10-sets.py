primer = {1,1,2,2,3,4}
primer.add(5)
primer.remove(1)
print(primer)
segundo= [3,4,5]
segundo = set(segundo)

print(segundo)
print(primer|segundo)
print(primer - segundo)
print(primer^segundo)

if 5 in segundo:
    print("hola mundo")