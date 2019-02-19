import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

# Convert deg to rad
rad = np.pi/180.0

# Parameters
n1 = 2.500
n2 = 1.333
th1 = sp.arcsin(n2/n1) # Incident critical angle
             # since the wave at the boundary will be evanescent
             # and propagate along the surface.
k1 = 10*np.pi*n1 # set wavelength equal to one
k2 = 10*np.pi*n2 # set wavelength equal to one

# Incident wave
xlist  = np.linspace(-1, 0, 1000)
ylist  = np.linspace(-1, 1, 1000)
X1, Y1 = np.meshgrid(xlist, ylist) # Create mesh: xlist X ylist
Z1     = np.cos(k1*(X1*np.cos(th1) + Y1*np.sin(th1)))
plt.figure()
plt.colorbar(plt.contourf(X1, Y1, Z1))

# Transmitted evanescent wave
xlist  = np.linspace(0, 1, 1000) # cover the transmitted region
X2, Y2 = np.meshgrid(xlist, ylist)
Z2     = (2*n1*np.cos(th1)/(n1*np.cos(th1)+1j*sp.sqrt(n1**2*np.sin(th1)**2-1))).real*np.exp(-X2)* \
         np.cos(k1*Y2*np.sin(th1))  # Pulled from Griffiths Electrodynamics 4th ed.
plt.contourf(X2, Y2, Z2)

plt.show()
