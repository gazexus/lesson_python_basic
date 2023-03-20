def test():
    a = int(input())
    if a > 0:
       positive()
    elif a < 0:
        negative()
def positive():
    print("Положительное!")

def negative():
    print("Отрицательное!")

test()