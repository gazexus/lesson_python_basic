a = [10, 20, 30, 40, 50, 60]
b = []
for id, item in enumerate(a):
    c = str(id) + " " + str(item)
    b.append(c)

print(b)