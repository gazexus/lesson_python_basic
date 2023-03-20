f1 = open('nums.txt')
n = f1.read()
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])

print(sum(n))

