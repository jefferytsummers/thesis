import matplotlib.pyplot as plt
from matplotlib.contour import *
from matplotlib.widgets import Slider, Button
import numpy as np
import scipy as sp


# Convert deg to rad
rad = np.pi/180.0

# Initial Parameters
n1 = 2.500
n20 = 1.0    # Initial index of transmitting medium
             # Will be varied with a slider
d_n2 = 0.05  # Transmitting index step for slider
                        # since the wave at the boundary will be evanescent
                        # and propagate along the surface.
k1 = 10*np.pi*n1  # set vacuum wavelength equal to one


def compute_and_plot(ax, n2):
    xlist1    = np.linspace(-1, 0, 100)
    xlist2    = np.linspace( 0, 1, 100) # cover the transmitted region
    ylist_i   = np.linspace(-1, 0, 100)
    ylist_r   = np.linspace( 0, 1, 100)
    ylist     = np.linspace(-1, 1, 100)
    x1, y1_i  = np.meshgrid(xlist1, ylist_i)
    x1, y1_r  = np.meshgrid(xlist1, ylist_r)
    x2, y2    = np.meshgrid(xlist2, ylist)
    th1       = sp.arcsin(n2/n1)
    # Incident wave
    Z1_i      = np.cos(k1*(x1*np.cos(th1) + y1_i*np.sin(th1)))
    Z1_r      = np.cos(k1*(x1*np.cos(th1) - y1_r*np.sin(th1)))
    # Reflected wave
    Z2        = (2*n1*np.cos(th1)/(n1*np.cos(th1)+1j*sp.sqrt(n1**2*np.sin(th1)**2-1))).real*np.exp(-x2)* \
          np.cos(k1*y2*np.sin(th1))  # Pulled from Griffiths Electrodynamics 4th ed.
    L = np.linspace(-1.0, 0, 50)
    plt.plot(L, -np.sin(th1)/np.cos(th1)*L, color='red')
    plt.plot(L, np.sin(th1)/np.cos(th1)*L, color='red')
    plt.vlines(0, -1, 1, colors='k')

    incident  = plt.contourf(x1, y1_i, Z1_i)
    reflected = plt.contourf(x1, y1_r, Z1_r)
    plt.colorbar(incident)
    transmitted = plt.contourf(x2, y2, Z2)

# Plot
fig1 = plt.figure()
plt.title("n2 = 1.0")
ax1 = fig1.add_subplot()
plt.xlim(-1,1)
plt.ylim(-1,1)
compute_and_plot(ax1, 1.0)
fig2 = plt.figure()
ax2 = fig2.add_subplot()
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.title("n2 = 2.0")
compute_and_plot(ax2, 2.0)

plt.show()
