import math
import os
import sys


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(f"Error. Expected a valid real number, got {e.args[0].split(':')[-1].strip()} instead")


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
    a = get_float_input("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = get_float_input("a = ")
    b = get_float_input("b = ")
    c = get_float_input("c = ")

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    roots = solve_quadratic(a, b, c)
    print(f"There are {len(roots)} roots")
    for i, root in enumerate(roots, 1):
        print(f"x{i} = {root}")


def file_mode(filepath):
    if not os.path.exists(filepath):
        print(f"file {filepath} does not exist")
        sys.exit(1)
    try:
        with open(filepath, 'r') as file:
            content = file.read().strip()
            a, b, c = map(float, content.split())
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
            print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
            roots = solve_quadratic(a, b, c)
            print(f"There are {len(roots)} roots")
            for i, root in enumerate(roots, 1):
                print(f"x{i} = {root}")
    except Exception:
        print("invalid file format")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python equation.py [file]")
        sys.exit(1)
