string1 = input('enter value1: ').split()
#string2 = input('enter value2: ').split()
string2 = map(int, input('enter value2: ').split())
#new_list = []
#for i in string2:
#     new_list.append(int(i))

new_dict = dict(zip(string1, string2))

print(new_dict)