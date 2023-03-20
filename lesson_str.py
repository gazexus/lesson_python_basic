a = 'HELLO World'
val_small = 0
val_big = 0
for i in a:
    if i.isupper():
        val_big += 1
    elif i.islower():
        val_small += 1

if val_big >= val_small:
    print(a.upper())
else:
    print(a.lower())



