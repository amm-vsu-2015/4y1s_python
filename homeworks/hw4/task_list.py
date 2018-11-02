
from sympy import *
import mpmath as mp
import numpy as np
import matplotlib
# create environment for matplotlib.
# only uses by pyenv
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# z01
"""
Найти в аналитическом виде сумму из n членов последовательности нечетных чисел, начиная от 1.
"""
i, n, m = symbols("i n m", integer = True)
res = summation(2*i - 1, (i, 1, n))
print(" [z01] res = ", res)


# z02
"""
Найти сумму членов бесконечной последовательности
1/3 + 1/3^2 + 1/3^3 + 1/3^4 + ...
a) в аналитическом виде с исп. sympy.summation;
b) в численном виде с исп. sympy.mpmath.nsum;
c) в численном виде с исп. while (машинная точность).
"""
#a
"""
бесконечность - sympy.mpmath.inf
"""
i, n, m = symbols("i n m", integer=True)
resa = summation(1/3**i, (i, 1, oo))
print(" [z02-a] resa = ", resa)

# b
# resb = inf(lambda n: 1/3**n, [1, inf])
# print(" [z02-b] resb = ", resb)

#c
s = 0.0 # обнуление сумматора
sn = 1.0
x = 1.0/3.0

while 1:
    sn *= x # текущий член ряда
    ss = s + sn
    if s == ss: break
    s = ss

print(" [z02-c] resc = ", s)


# z03
"""
Найти предел последовательности (1 + 1/n)**n, n=1,2,3,...
Syntax: limit(function, variable, point)
"""
n = symbols("n", integer = True)
res = limit((1 + 1/n)**n, n, oo)
print(" [z03] res = ",res)


# z04
"""
Найти предел x**x при x -> 0
Syntax: limit(function, variable, point)
"""
x = symbols("x", real = True)
res = limit(x**x, x, 0)
print(" [z04] res = ",res)

# z05
"""
Найти предел ln(1+sin(4x))/(exp(sin(5x))-1) при x -> 0
sympy.mpmath.log(x, b)
Computes the base-b logarithm of x, logb(x).
If b is unspecified, log() (page 561) computes
the natural (base e) logarithm and is equivalent to ln()
"""
x = symbols("x", real = True)

def w(x):
    return ln(1 + sin(4*x)) / (exp(sin(5*x)) - 1)

res = limit(w(x), x, 0)
print(" [z05] res = ", res)


# z06
"""
Найти предел n/(n!)**(1/n) при n -> oo
"""
n = symbols("n", integer = True)
res = limit(n / factorial(n)**(1/n), n, oo)
print(" [z06] res = ", res)


# z07
"""
Найти предел функции
ln(1 + sin(4x))/(exp(sin(5x))-1) при x -> 0
log()
mpmath.log(x, b)
Computes the base-b logarithm of x, log_b(x). If b is unspecified, log() computes the natural (base e) logarithm and is equivalent to ln()
"""
x = symbols("x", real = True)
f = lambda x: ln(1 + sin(4*x)) / (exp(sin(5*x)) - 1)
res = limit(f(x), x, 0)
print(" [z07] res = ", res)


# z08
"""
Определить, имеет ли функция |2 x - 3|/(2 x - 3) скачок при x = 3/2. Если имеет, то чему он равен.
"""
x = symbols("x", real = True)
f = lambda x: abs(2*x - 3)/(2*x - 3)
res1 = limit(f(x), x, 3/2, dir="+")
res2 = limit(f(x), x, 3/2, dir="-")
print(" [z08] res1 = ", res1, " res2 = ", res2, " res = ", res1 - res2)


# z09
"""
Вывести численные значения числа Пифагора и основания натурального алгоритма
"""
# x = Symbol("x", real=True)
print(" [z09] res1 = ", pi.evalf(), " res2 = ", E.evalf())


# z10
"""
Раскрыть скобки (x+y)**3
"""
x, y = symbols("x y")
res = expand((x+y)**3)
print(" [z10] res = ", res)


# z11
"""
Раскрыть скобки (x+y)**3
"""
x, y = symbols("x y")
res = expand(cos(3*x), trig = True)
print(" [z11] res =", res)


# z12
"""
Раскрыть скобки (x+y)**3
"""
x, y = symbols("x y")
res = expand((x+y)**3)
print(" [z12] res = ", res)


# z13
"""
Упростить выражение
cos(x)cos(y) - sin(x)sin(y) с помощью simplify
"""
x, y = symbols("x y")
res = simplify(cos(x)*cos(y) - sin(x)*sin(y))
print(" [z13] res = ", res)


# z14
"""
Найти производную функции sin(x)ln(x).
"""
x = symbols("x")
res = diff(sin(x)*ln(x), x)
print(" [z14] res = ", res)


# z15
"""
Найти 3-ю производную функции x**x.
"""
x = symbols("x")
res = diff(x**x, x, 3)
print(" [z15] res = ", res)


# z16
"""
Найти численное значение производной функции sin(x + pi/5)^2 при x=1.
N() is equivalent to evalf()
"""
x = symbols("x")
res = diff(sin(x + pi/5)**2, x, 1).subs(x, 1).evalf()
print(" [z16] res = ", res)


# z17
"""
Разложить в ряд Тейлора функцию sin(2x)/cos(x) в окрестности точки x=0 до члена с x**11 включительно.
"""
x = symbols("x")
f = sin(3*x)/cos(x)
res = f.series(x, 0, 12)
print(" [z17] res = ", res)



# z18
"""
Найти неопределённый интеграл от ф-ии sin(3x). Выполнить проверку.
"""
x = symbols("x")
f = lambda x: sin(3*x)
res = integrate(f(x), x)
print(" [z18] res = ", res)
# проверка
print(diff(res, x))


# z19
"""
Найти неопределённый интеграл от ф-ии exp(-x**2)erf(x).
"""
x = symbols("x")
f = lambda x: exp(-x**2) * erf(x)
res = integrate(f(x), x)
print(" [z19] res = ", res)
# проверка
print(diff(res, x))


# z20
"""
Найти определённый интеграл от ф-ии exp(-x**2). Пределы интегрирования от -oo до +oo.
"""
x = symbols("x")
res = integrate(exp(-x**2), (x, -oo, oo))
print(" [z20] res = ", res)


# z21
"""
Найти аналитическое решение ОДУ
f''(x) + f(x) = 0
"""
f = Function('f')
x = symbols('x')
res = dsolve(f(x).diff(x, x) + f(x), f(x))
print(" [z21] res = ", res)


# z22
"""
Найти аналитическое решение алгебраического уравнения x**4 = 1.
"""
x = symbols("x")
res = solve(x**4-1, x)
print(" [z22] res = ", res)

# z23
"""
Найти аналитическое решение системы алгебраических уравнений x + 5*y - 2 = 0;
3*x - 6*y + 15 = 0.
"""
x, y = symbols("x, y")
res = solve([x + 5*y - 2, 3*x - 6*y + 15], [x, y])
print(" [z23] res = ", res)


# z24
"""
Построить графики функций x*sin(x) и sin(3x)/x (x ε[-6, +6]) на одних координатных осях.
"""
ff = lambda xx: 3.0 if abs(xx) < 1.e-12 else np.sin(3*xx)/xx

nt = 101
x = np.linspace(-6.0, 6.0, nt)

y1 = x*np.sin(x)
y2 = [ff(x[i]) for i in range(nt)]

# plt.fill(x, y1, 'r')
plt.plot(x, y1, 'r', linewidth = 3.0, label = "y1(x)")
plt.plot(x, y2, 'b', linewidth = 3.0, label = "y2(x)" )
plt.grid(True)
plt.xlabel("X", fontsize = 16, color = "k")
plt.ylabel("Y1(X), Y2(X)", fontsize = 16, color = "k")
plt.legend(fontsize = 16)
plt.savefig("graph.pdf")
plt.show()
