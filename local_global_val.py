result = 0
def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b
    #print("Площадь: %.2f" % (a * b))

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h
    #print("Площадь: %.2f" % (0.5 * a * h))


figure = input("1 - прямоугольник, 2 - треугольник: ")
if figure == "1":
    rectangle()
elif figure == "2":
    triangle()

print("Площадь: %2.f" % result)