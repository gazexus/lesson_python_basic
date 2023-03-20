import random

d = input("1 - int, 2 - float: ")

if d == '1':
    a = int(input("enter value: "))
    b = int(input("enter value: "))
    print("Number int: ", random.randint(a, b))
elif d == '2':
    a = float(input("enter value: "))
    b = float(input("enter value: "))
    n = random.random() * (b + a) + a
    print("Number float: ", round(n, 2))


#print(random.randrange(6, 12))

#print(random.randrange(5, 100, 5))