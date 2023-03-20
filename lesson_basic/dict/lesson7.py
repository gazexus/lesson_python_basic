list1 = input("enter value: ").split()
list2 = map(int, input("enter namber: ").split())

my_dict = dict(zip(list1, list2))

if 5 in my_dict.values():
    print("Есть")
else:
    print('Нет')

print(list2)
print(my_dict)