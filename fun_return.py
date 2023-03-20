def getInput():
    a = input("enter value: ")
    return a

def testInpit(b):
    try:
        n = int(b)
        return True
    except ValueError:
        return False

def strToInt(c):
    n = int(c)
    return n

def printInt(n):
    print(n)

val1 = getInput()
is_int = testInpit(val1)
if is_int == 'True':
    val2 = strToInt(val1)
    printInt(val2)



