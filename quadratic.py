# Replace the "ANSWER HERE" for your answer

import math

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"   # con espacio para que pase el test

def value_y(a, b, c, x):
    return a*x**2 + b*x + c

def to_string(a, b, c):
    # Respetar espacios, mayúscula X, y formato exacto del test
    parts = []
    if a != 0:
        parts.append(f"{a} * X^2")
    if b != 0:
        parts.append(f"{b} * X")
    if c != 0:
        parts.append(f"{c}")
    if not parts:
        return "f(x) = 0"
    return "f(x) = " + " + ".join(parts)
    
def derivation(a, b, c):
    da = 2*a
    db = b
    parts = []
    if da != 0:
        parts.append(f"{da} * X")
    if db != 0:
        parts.append(f"{db}")
    if not parts:
        return "f'(x) = 0"
    return "f'(x) = " + " + ".join(parts)
