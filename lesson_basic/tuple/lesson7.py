my_tuple = tuple(input("enter value: ").split())

result = all(i == my_tuple[0] for i in my_tuple)
print(result)
