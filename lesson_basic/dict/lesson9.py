my_dict = {}

for i in range(3):
    value_ = input().split()
    for k, *v in [value_]:
        my_dict[k] = v

city = input("enter city: ")

for k, v in my_dict.items():
    if city in v:
        print(k)
#my_dict = {k:v for _ in range(3) for k, *v in  [input().split()]}

