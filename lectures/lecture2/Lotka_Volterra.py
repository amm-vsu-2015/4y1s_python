# -*- coding: cp1251 -*-
"""
Lotka�Volterra using scipy.integrate.odeint:

dx/dt = x*(alpha - beta*y);
dy/dt =-y*(gamma - delta*x);
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
alpha=0.1
beta=0.015
gamma=0.0225
delta=0.02

def system(z,t):
   x,y=z[0],z[1]
   dxdt= x*(alpha-beta*y)
   dydt=-y*(gamma-delta*x)
   return [dxdt,dydt] # посчитали правую часть ДУ и вернули

#
t=np.linspace(0,300.,1000)
x0,y0=1.0,1.0
sol=odeint(system,[x0,y0],t)
X,Y=sol[:,0],sol[:,1]
# изобразить график по массивам X, Y, синим цветом с тонкой линией (толщиной 5)
plt.plot(X,Y,'b-', linewidth=5)
# вывести сетку на графике
plt.grid(True)
# изображение легенды на графике
plt.xlabel("x"); plt.ylabel("y")
# сохранить график в файл
plt.savefig('y1.pdf',dpi=300)
# показать график на экране
plt.show()
