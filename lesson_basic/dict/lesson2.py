string_numder = map(int, input("enter value: ").split())

my_dict = {}

for n in string_numder:
    if n % 2 == 0:
        my_dict[n] = 'четное'

print(my_dict)