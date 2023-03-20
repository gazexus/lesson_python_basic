import square

square_val = input("1 - rectangle, 2 - triengle, 3 - circle:  ")

if square_val == '1':
    a = float(input("enter value a: "))
    b = float(input("enter value b: "))
    print("square rectangle: ", square.rectangle(a, b))
elif square_val == '2':
    a = float(input("enter value a:"))
    h = float(input("enter value h:"))
    print("square triengle: ", square.triengle(a, h))
elif square_val == '3':
    r = float(input("enter value r: "))
    print("square circle: ", square.circle(r))
else:
    print("Error")