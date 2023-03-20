string_ = input("enter value: ").split()

my_set = set()

for i in string_:
    if i.lower().endswith('.jpg'):
        my_set.add(i.lower())

print(*sorted(my_set))