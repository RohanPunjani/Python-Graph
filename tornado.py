# making a tornado figure in graph
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(0 * np.pi, 10 * np.pi, 200)
z = np.linspace(0, 10, 200)
r = z ** 2 + 1
x, y = {}, {}

for i in range(0, 10):
    x[i] = r * np.sin(theta + (9*i))
    y[i] = r * np.cos(theta + (9*i))
    l = "Tornado", i+1
    ax.plot(x[i], y[i], z, label=l)

ax.legend()
plt.show()
