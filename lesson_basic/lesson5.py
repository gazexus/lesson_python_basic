n = int(input('enter value: '))
years = n // 365
mouths = (n - years * 365) // 30
days = (n - years * 365 - mouths * 30)
print(years)
print(mouths)
print(days)