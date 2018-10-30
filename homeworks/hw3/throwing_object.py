"""
Movement along z-axis (perpendiculary surface)
dz(t)/dt = v(t)
dv(t)/dt = -g - (A*v(t) + B*v(t)^3)/m
"""

import numpy as np
import matplotlib
# create environment for matplotlib.
# only uses by pyenv
matplotlib.use('TkAgg')
from scipy.integrate import odeint
import matplotlib.pyplot as plot

startPosition = 0.0  # m
startSpeed = 500.0   # m/sec
mass = 0.009   # kg
gravity = 9.8  # m/sec^2
A = 1.e-5      # N*sec/m
B = 1.e-8      # N*sec^3/m^3
maxThrowingTime = 110.0  # - не имеет значения размер

# вычисление правых частей уравнения
def solveDiff(f, t):
    global mass, gravity, A, B
    dzdt = f[1]
    dvdt = -gravity - (A * dzdt + B * dzdt**3)/mass
    return [dzdt, dvdt]

# path analyzes and return some points
def analyzePath(time, positions):
    throwingTime = 0.0
    maxHeight = 0.0
    climbTime = 0.0
    downTime = 0.0

    for idx in range(0, len(time) - 1, 1):
        if positions[idx] >= 0.0:
            throwingTime = time[idx]

        if positions[idx] >= maxHeight:
            maxHeight = positions[idx]
            climbTime = time[idx]

        downTime = throwingTime - climbTime

    return [throwingTime, maxHeight, climbTime, downTime]

segmentsCount = 1000 # nt
# от 0 до maxThrowingTime разбиваются на segmentsCount узлов
time = np.linspace(0., maxThrowingTime, segmentsCount) # t
# вычисляем ДУ
differentialResult = odeint(solveDiff, [startPosition, startSpeed], time)
positions = differentialResult[:, 0]
speeds = differentialResult[:, 1]

(throwingTime, maxHeight, climbTime, downTime) = analyzePath(time, positions)

print(" [!] Max height is %02d" % maxHeight)
print(" [!] throwing time is %02d" % throwingTime)
print(" [!] climb time is %02d" % climbTime)
print(" [!] dropping down time is %02d" % downTime)

diff = abs(climbTime - downTime)

if climbTime >= downTime:
    print(" [!] Climbing time is longer than dropping down time and equals is %2d" % diff)
else:
    print(" [!] Dropping down time is longer than climbing time and equals is %2d" % diff)

# строим график
plot.plot(time, speeds, 'r-', linewidth = 3) # график скорости
plot.plot(time, [0.0] * segmentsCount, 'g-', linewidth = 1) # график z(t)
# задаем график
plot.axis([0, maxThrowingTime, -250., 500.])
# выводим сетку на графике
plot.grid(True)
# легенда
plot.xlabel("time")
plot.ylabel("speed(time)")
# сохранить в файл
plot.savefig("graph_speed.pdf", dpi = 300)
# вывести
plot.show()

plot.plot(time, positions,'b-', linewidth = 3)
plot.axis([0, throwingTime, 0., maxHeight])
plot.grid(True)
plot.xlabel("time")
plot.ylabel("height(time)")
plot.savefig("graph_throwing.pdf", dpi = 300)
plot.show()
