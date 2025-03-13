import math


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []


def interactive_mode():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    roots = solve_quadratic(a, b, c)
    print(f"There are {len(roots)} roots")
    for i, root in enumerate(roots, 1):
        print(f"x{i} = {root}")


if __name__ == "__main__":
    interactive_mode()
