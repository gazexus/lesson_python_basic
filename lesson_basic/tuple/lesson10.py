n = int(input("enter value: "))
position = []

for i in range(n):
    position.append(tuple(map(int, input("enter cord: ").split())))

max_cord = max(position, key= lambda x: x[0] ** 2 + x[1] ** 2)
print(max_cord)
print(position)