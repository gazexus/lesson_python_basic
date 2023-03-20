a = ''
while a.isdigit() == False:
    a = input('enter number 1: ')
b= ''
while b.isdigit() == False:
    b = input('enter number 2: ')

sum = int(a) + int(b)
print(sum)