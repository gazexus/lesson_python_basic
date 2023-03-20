a = input("Entre first value: ")
b = input("Enter second value: ")
try:
    a = int(a)
except ValueError:
    print("Result: ", a + b)
else:
    try:
        b = int(b)
    except ValueError:
        a = str(a)
    finally:
        print("Result:", a + b)
