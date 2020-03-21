from matplotlib import pylab as plt
import numpy as np
from numpy import sin
from numpy import exp
x1=1.
x2=4.
x3=10.
x4=15.
y1=sin(x1/5.)*exp(x1/10.)+5*exp(-x1/2.)
y2=sin(x2/5.)*exp(x2/10.)+5*exp(-x2/2.)
y3=sin(x3/5.)*exp(x3/10.)+5*exp(-x3/2.)
y4=sin(x4/5.)*exp(x4/10.)+5*exp(-x4/2.)
b=np.array([[y1],[y2],[y3],[y4]])
A=np.array([[1,x1,x1**2,x1**3],[1,x2,x2**2,x2**3],[1,x3,x3**2,x3**3],[1,x4,x4**2,x4**3]])

A1=np.linalg.inv(A)
w=np.dot(A1,b)
w0=w[0,0]
w1=w[1,0]
w2=w[2,0]
w3=w[3,0]

x=np.arange(1, 15)
y=x**3*w3+x**2*w2+x*w1+w0
plt.plot(x, y)
plt.show()

w0=round(w0,2)
w1=round(w1,2)
w2=round(w2,2)
w3=round(w3,2)

print w0,w1,w2,w3
