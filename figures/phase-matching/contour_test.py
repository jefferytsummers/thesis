import numpy as np
import matplotlib as mpl
import matplotlib.mlab as mlab
import matplotlib.pyplot as pyl
from matplotlib.contour import QuadContourSet
from matplotlib.widgets import Slider

#Define display parameters
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'
delta = 0.1

#Define model parameters
alpha = 1.50
v = np.arange(-1, 1, delta)
w = np.arange(-1, 1, delta)

def compute_and_plot(ax, alpha):
    #Calculate grid values
    th1=np.arcsin(alpha/2.5)
    V, W = np.meshgrid(v,w)
    U = np.cos(2*np.pi*(V*np.cos(th1)+W*np.sin(th1)))

    CS = QuadContourSet(ax, V, W, U, 50)
#    pyl.clabel(CS, inline=1, fontsize=10)
    pyl.contourf(CS)

# Plot
fig = pyl.figure()
pyl.title('Simplest default with labels')
ax = fig.add_subplot(111)
compute_and_plot(ax, alpha)

#Define slider for alpha
axcolor = 'lightgoldenrodyellow'
alpha_axis  = pyl.axes([0.25, 0.01, 0.55, 0.03], facecolor=axcolor)
alpha_slider = Slider(alpha_axis, 'Amp', 1.0, 2.45, valinit=1.5)

def update(ax, val):
    alpha = alpha_slider.val
    ax.cla()
    compute_and_plot(ax, alpha)
    pyl.draw()

alpha_slider.on_changed(lambda val: update(ax, val))

pyl.show()
