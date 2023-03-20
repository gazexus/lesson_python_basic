enter_str = input("Enter string: ")

if len(enter_str) > 10:
    print("Строка длинее 10 символов!")
else:
    diff = 10 - len(enter_str)
    enter_str = enter_str + '*' * diff
    print(enter_str)