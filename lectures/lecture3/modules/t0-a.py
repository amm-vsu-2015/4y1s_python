

import mod_a1 as a1
import mod_a2 as a2
import numpy as np
import matplotlib
# create environment for matplotlib.
# only uses by pyenv
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def f(x):
    return (x-1.5)*(x+1.1)*(x-2.2)

x1 = -1.2
x2 = +2.3
n = 101

x = np.linspace(x1, x2, n)
plt.plot(x, f(x), 'r-', linewidth=2)
font = {'family': 'serif', 'color': 'blue', 'weight': 'normal', 'size': 16}
plt.title('Test for roots', fontdict=font)
plt.xlabel('x', fontdict=font)
plt.ylabel('f(x)', fontdict=font)
plt.grid()
plt.show()

xx1 = 1.0
xx2 = 1.7
eps = 1.e-5
r = a2.bisection(f, xx1, xx2, eps)
temp = a2.info(r)

############################

x1 = 0.0
x2 = 6.0
n = 101

x = np.linspace(x1, x2, 101)

y1 = a1.fun2(x)
y2 = a1.fun3(1, x)

plt.subplot(2, 1, 1)
plt.plot(x, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.xlabel('x')
plt.ylabel('y1(x)')

plt.subplot(2, 1, 2)
plt.plot(x, y2, 'r.-')
plt.xlabel('x')
plt.ylabel('y2(x)')

plt.show()
