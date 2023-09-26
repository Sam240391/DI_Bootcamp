
nombre = int(input("Entrez un nombre : "))

diviseurs = []

for i in range(1, nombre):
    if nombre % i == 0:
        diviseurs.append(i)

print(f"Les diviseurs de {nombre} exepté lui meme sont : {diviseurs}")

diviseursSum = sum(diviseurs)

if diviseursSum == nombre:
    print(True) 
else:
    print(False)
