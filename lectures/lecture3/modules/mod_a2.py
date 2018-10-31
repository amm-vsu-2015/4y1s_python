"""
module mod_a2
"""

def bisection(f, a, b, tol):
    c = (a + b)/2.0
    while (b-a)/2.0 > tol:
        if abs(f(c)) < tol: return c
        elif f(a)*f(c) < 0: b=c
        else: a = c
        c=(a+b)/2.0
    return c


def info(x):
    s = "Function f(x) has the root: x = "
    print(s, x)
    return()