first_number = set(input("enter number1: "))
second_number = set(input("enter number2: "))

print(first_number)
print(second_number)
if first_number.intersection(second_number):
    print("yes")
else:
    print("no")
