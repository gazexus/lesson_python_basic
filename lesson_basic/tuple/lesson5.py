nested_tuple = ((12, 3, 1), (5, 11), (15, 7, 8, 9), (10, 6, 4))
res = []
for i in nested_tuple:
    res.extend(i)

print(tuple(sorted(res)))
