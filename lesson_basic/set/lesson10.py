m, n = int(input("enter m: ")), int(input("enter n: "))

pantry = set()
result = []

for _ in range(m):
    entre_pantry = input("enetr pantry: ").lower()
    pantry.add(entre_pantry)
#print(pantry)
for _ in range(n):
    entre_ingrid = input("enter ingrit: ").lower()
    if entre_ingrid in pantry:
        result.append("есть")
    else:
        result.append("Отсутствует")

print(*result, sep='\n')


