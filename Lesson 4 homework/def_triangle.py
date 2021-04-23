def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def is_it_triangle(a, b, c):
    if triangle(a, b, c):
        return "This is a triangle"
    else:
        return "Not a triangle"


if __name__ == "__main__":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    print(triangle(a, b, c))
    print(is_it_triangle(a, b, c))


def triangle_type_by_sides(a, b, c):
    if triangle(a, b, c):
        if a == b == c:
            return "Equilateral triangle"
        elif a != b != c:
            return "Versatile triangle"
        elif a == b or a == c or b == c:
            return "Isosceles triangle"
    else:
        return "Not a triangle"


if __name__ == "__main__":
    print(triangle_type_by_sides(a, b, c))
