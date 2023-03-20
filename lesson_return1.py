def mult_fun():
    a = 1
    n = int(input())
    if n == 0:
        a = 0
    while n != 0:
        a *= n
        n = int(input())
    return a

print(mult_fun())