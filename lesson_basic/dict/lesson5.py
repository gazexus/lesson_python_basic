my_list = input("enter value: ").split('; ')
print(my_list)
dict_my = {}
#sp = [[i.split(', ')[0], i.split(',')[1]] for i in my_list]
sp = []
for i in my_list:
    sp.append([i.split(', ')[0], i.split(', ')[1]])
print(sp)
for v, k in sp:
    dict_my[k] = v
print(dict_my)

for k, v in dict_my.items():
    result = f'{k}: {v}'
    print(result)

