user1 = set(input("enter value1: ").split())
user2 = set(input("enter value2: ").split())

new_set1 = user1.union(user2)
new_set2 = user1.intersection(user2)
result = (len(new_set2) / len(new_set1)) * 100
print(f'Совпадение интересов: {result:.2f}%')
print(new_set1)
print(new_set2)