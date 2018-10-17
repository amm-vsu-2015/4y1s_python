"""
lotka_volterra using scipy.integrate.odeint:

dx/dt = x*(alpha - beta*y);
dy/dt =-y*(gamma - delta*x);
"""
import numpy as np
import matplotlib
# create environment for matplotlib.
# only uses by pyenv
matplotlib.use('TkAgg')

from scipy.integrate import odeint
import matplotlib.pyplot as plot

alpha = 0.1; beta = 0.015; gamma = 0.0225; delta = 0.02

# посчитать правую часть ДУ
def solveRightPart(z, t):
   x = z[0]
   y = z[1]
   dxdt= x*(alpha-beta*y)
   dydt=-y*(gamma-delta*x)
   return [dxdt, dydt]

# время в виде массива элементов от 0 до 300, разбитое равно на 1000 элементов
time = np.linspace(0, 300., 1000)
# начальные условия уравнения
x0 = 1.0
y0 = 1.0

# подсчет производной
differentialResult = odeint(solveRightPart, [x0, y0], time)
# значения прозводной в каждый момент времени time
values = differentialResult[:, 1]
# значения времени для производных values
times = differentialResult[:, 0]

# изобразить график по массивам X, Y (или values, times),
# синим цветом с тонкой линией (толщиной 5)
# сначала аргументы, потом значения
plot.plot(values, times, 'b-', label='y\'')
# print legends
plot.legend()
# начертить определенную сетку графика
plot.axis([0., 50., 0., 50.])

# вывести сетку на графике
plot.grid(True)
# изображение легенды на графике
plot.xlabel('x'); plot.ylabel('y')
# сохранить график в файл
plot.savefig('differential_equation.pdf', dpi = 300)
# показать график на экране
plot.show()


# x(t)
plot.plot(time, values, 'r-', label='x(t)')
# y(t)
plot.plot(time, times, 'g-', label='y(t)')
# print legends
plot.legend()
# начертить определенную сетку графика
plot.axis([0., 50., 0., 50.])

# вывести сетку на графике
plot.grid(True)
# изображение легенды на графике
plot.xlabel('x'); plot.ylabel('y')
# сохранить график в файл
plot.savefig('differential_parameters.pdf', dpi = 300)
# показать график на экране
plot.show()
