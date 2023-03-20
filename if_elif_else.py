try:
    old = int(input("You are age? "))
except ValueError:
    print("Ввели не целое число!")
    quit()
print("Recommended: ", end='')

if 3 <= old < 6:
    print('"Заец в лаберинте."')
elif 6 <= old < 12:
    print('"Марсианин."')
elif 12 <= old < 16:
    print('"Загадочный остров."')
elif 16 <= old:
    print('"Поток сознания."')
else:
    print('-')

