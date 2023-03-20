sp_number = input("enter list: ").split(';')
name = input("enetr name: ")
sp = []
my_dict = {}
for i in sp_number:
    sp.append([i.split()[0], i.split()[1]])
for k, v in sp:
    my_dict[k] = v


print(my_dict.get(name, 'Нет такого абонента'))

#print(sp)
#print(my_dict)