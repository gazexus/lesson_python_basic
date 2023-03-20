my_list = input("enter value: ").split()
new_list = []
for i in my_list:
    if i.isalpha():
        new_list.append(i)
new_list.sort(key=len)

print(*new_list, sep='\n')
