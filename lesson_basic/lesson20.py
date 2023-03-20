my_string = input("enter value").split(',')
even = []
no_even = []
for i in my_string:
    if int(i)%2 != 0:
        no_even.append(i)
    else:
        even.append(i)

print(*even)
print(*no_even)
