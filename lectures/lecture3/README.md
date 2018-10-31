## Пользовательские модули и пакеты

Подключение модуля:

```python
import matplotlib.pyplot as plt
```

Пример создания и использования пользовательского модуля в папке [modules](https://github.com/amm-vsu-2015/4y1s_python/tree/master/lectures3/modules/):


Терминология:

```
Абсолютная точность – когда приближение к точке (например, при поиске предела) ограничивается заданной заранее эпсилон-точностью.
Машинная точность – когда точность ограничивается битовой сеткой типов (float/double).

float = 32bit value with 7-8 bit of mantissa
double = 64bit value with 15-16 bit of mantissa

s = 1.5; # float by default
s2 = s;

s = s + 1.e-17 # more than 16 bit

s == s2 # digits are equals because we are changed 17th bit thats not included for float values

Поэтому обычно объявляется некоторый "сумматор", состоящий из членов ряда.

# посчитать сумму ряда для последовательности 1/3^n от 0 до бесконечности.

sum = 0.0
sn = 1.0
x = 1.0/3.0

while 1:
  sn *= x # текущий член ряда
  tmp = sum + sn
  if sum == tmp: break # это будет равным, когда отрезки станут меньше допустимой битовой сетки
  sum = tmp

print("reuslt: ", sum)


ДЗ, вариант 4 в z-15.pdf.
```

Лямбда-функции:

```python

def f(x):
  return numpy.sin(x)

# is equals

s = lambda n: numpy.sin(x)

# uses as

s(n)

```

### Домашнее задание

[Ссылка на домашнее задание](https://github.com/amm-vsu-2015/4y1s_python/tree/master/homeworks/hw3)
