text = 'аиеёоуыэюя'
my_list = input().split()
list1 = []
list2 = []

for i in my_list:
    if i[0] in text:
        list1.append(i)
    else:
        list2.append(i)
print(*list1)
print(*list2)
