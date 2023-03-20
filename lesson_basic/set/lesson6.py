my_stirng1 = set(map(int, input("enter namber1:").split()))
my_stirng2 = set(map(int, input("enter namber2:").split()))



result = my_stirng1.intersection(my_stirng2)
print(*sorted(result))

