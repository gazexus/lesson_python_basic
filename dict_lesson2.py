def dict_new (obj):
    d = {}
    for i, j in obj:
        d[j] = i
    return d

a = {1:'red', 2:'green', 3:'yellow', 4:'blue'}
dict_items = dict_new(a.items())
print(a)
print(dict_items)