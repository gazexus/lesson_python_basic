numbers = ((5, 4, 5, 4), (3, 3, 4, 6), (8, 9, 5, 4), (12, 4, 5, 1), (9, 3, 5, 1))
avg = tuple(sum(i) / len(i) for i in numbers)

#s1, s2, s3, s4, s5 = numbers
#my_tuple = ((sum(s1) / 4), (sum(s2) / 4))
print(*avg)

