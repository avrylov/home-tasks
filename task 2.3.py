from matplotlib import pylab as plt
import numpy as np
from numpy import sin
from numpy import exp
from scipy import optimize


def f(x):
    return sin(x/5.)*exp(x/10.)+5*exp(-x/2.)
def h(x):
    return f(x).astype(int) #чуть не колнчил, когда понял как это сделать

x_min1=optimize.minimize(h, [30], method='BFGS')
print x_min1
print h(30)

x2=[1,30]
x_min2=optimize.differential_evolution(f, [x2])
print x_min2
print h(25.88019277)