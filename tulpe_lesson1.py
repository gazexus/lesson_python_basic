from random import randint

def create_Tuple (begin, end):
    l = []
    for i in range(10):
        l.append(randint(begin, end))
    return tuple(l)

f = create_Tuple(0, 5)
s = create_Tuple(-5, 0)
f_s = f + s
count_zero = f_s.count(0)
print(f_s)
print(count_zero)
