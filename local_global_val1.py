s_circle = 0
def cylinder():
    def circle():
        global s_circle
        s_circle = 3.14 * r ** 2
    r = float(input("Радиус: "))
    h = float(input("Высота: "))
    s_cylinder = 2 * 3.14 * r * h
    if input("Боковую 1,  Полную 2: ") == "2":
        circle()
        s_cylinder += 2 * s_circle
    print(s_cylinder)

cylinder()