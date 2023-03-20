string = input("enter value: ").lower()
my_dict = {}
my_list = []
for i in string:
    my_dict[i] = string.count(i)
print(my_dict)
for k, v in my_dict.items():
    my_list.append(str(k) + '-' + str(v))

print(*my_list)