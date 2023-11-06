#!/usr/bin/env python3
# Created By: Meshach Wallace
# Date: NOV 3, 2023
# Finds the roots of a Parabola, using the quadratic equation.
import math


def main():
    print("Today we will be finding the roots of a parabola")
    a = float(input('Enter coefficient "a": '))
    b = float(input('Enter coefficient "b": '))
    c = float(input('Enter coefficient "c": '))

    # Calculate discriminant and find roots
    d = (b**2) - (4 * a * c)

    # Check the value of d and calculate the roots accordingly
    if d < 0:
        print("d is less than zero, so we will use the quadratic formula")
        p = (-b + math.sqrt(d)) / (2 * a)
        q = (-b - math.sqrt(d)) / (2 * a)
        print("The two possible roots are", p, "and", q)
    elif d > 0:
        print("d is greater than zero")
        # Use the quadratic formula to calculate roots
        p = (-b + math.sqrt(d)) / (2 * a)
        q = (-b - math.sqrt(d)) / (2 * a)
        print("The two real roots are", p, "and", q)
    elif d == 0:
        print("d is equal to zero, there is one real root:", -b / (2 * a))
    else:
        print("No real roots exist for these coefficients.")


if __name__ == "__main":
    main()
