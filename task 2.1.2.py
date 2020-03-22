from matplotlib import pylab as plt
import numpy as np
from numpy import sin
from numpy import exp
from scipy import optimize

def f(x):
    return sin(x/5.)*exp(x/10.)+5*exp(-x/2.)

 
x_min1=optimize.minimize(f, [2.], method='BFGS')
print x_min1
print round(f(4.13627628),2)

x_min2=optimize.minimize(f, [30.], method='BFGS')
print x_min2
print round(f(25.88019321),2)

x3=[1.0,30.]
x_min3=optimize.differential_evolution(f, [x3])
print x_min3
print round(f(25.88019234),2)

x=[1,30]
h=int(sin(x/5.)*exp(x/10.)+5*exp(-x/2.))
plt.plot(x, h)
plt.show()
