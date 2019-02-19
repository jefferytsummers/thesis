from mpl_toolkits import mplot3d
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#fig = plt.figure()
#ax = plt.axes(projection='3d')
# Parameters
n1  = 1.5
n2  = 1.0
rad = np.pi/180.0  # convert to radians
th1 = 30*rad
th2 = np.arcsin((n1/n2)*np.sin(th1))

# Data for a 3D trajectory
# Incoming planewave
k1      = 10*np.pi*n1
x1      = np.linspace(-1, 0, 1000)
y1      = np.linspace(-1, 1, 1000)
X1, Y1  = np.meshgrid(x1, y1)
z1      = np.cos(k1*(X1*np.cos(th1)+Y1*np.sin(th1)))
# Outgoing planewave
k2      = 10*np.pi*n2
x2      = np.linspace(  0, 1, 1000)
y2      = np.linspace(-1, 1, 1000)
X2, Y2  = np.meshgrid(x2, y2)
z2      = np.cos(k2*(X2*np.cos(th2)+Y2*np.sin(th2)))

plt.figure()
plt.colorbar(plt.contourf(X1, Y1, z1))
plt.contourf(X2, Y2, z2)

plt.show()
