# Quadratic Equation Solver

This application solves quadratic equations of the form:

```
ax^2 + bx + c = 0
```

where `a`, `b`, and `c` are real numbers, with `a ≠ 0`.

## Usage

### Interactive Mode

Run the program without arguments and enter the coefficients manually:

```sh
python main.py
```

Example output:

```
a = 2
b = 4
c = 2
Equation is: (2.0) x^2 + (4.0) x + (2.0) = 0
There is 1 root
x1 = -1.0
```

### File Mode

Provide the path to a file containing the coefficients:

```sh
python main.py input.txt
```

Example file format (`input.txt`):

```
1 0 -4
```

Execution result:

```
Equation is: (1.0) x^2 + (0.0) x + (-4.0) = 0
There are 2 roots
x1 = -2.0
x2 = 2.0
```

## Revert Commit

Commit: [1fdfd9d](https://github.com/vladosadchuk/mtsd-lab1/commit/ec81322a1acdcecbfa3b4dafc4c8ffff6b459b31)
