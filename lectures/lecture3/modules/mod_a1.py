"""
module mod_a1
"""
import numpy as np
from scipy import special


def fun1(x):
    res = np.sin(x)*np.exp(-(x-1)**2)
    return res


def fun2(x):
    res = fun1(x)*special.erf(x)
    return(res)


def fun3(n, x):
    res = np.abs(np.sin(x/3))*special.jn(n, x)
    return res
