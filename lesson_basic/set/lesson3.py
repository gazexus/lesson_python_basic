new_string = input("enter string").lower()

new_set = set()
for i in new_string:
    if i.isalpha():
        new_set.add(i)
if len(new_set) == 33:
    print("yes")
else:
    print("no")

print(new_set)