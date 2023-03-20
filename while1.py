n = input("enter number: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("not number")
        n = input("enter number: ")
if n % 2 == 0:
    print("Even")
else:
    print("not even")

