from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def f(x,y,R = 10,a = 1.,b = 1.):
    ans = (a*(x**2))-(b*(y**2))-(R**2)
    return ans
    
fig = plt.figure()
ax = fig.add_subplot(111, projection ='3d')
x = y = np.linspace(-5,5,100)
xv, yv = np.meshgrid(x,y)
z = f(xv, yv)
#ax.plot_wireframe(xv, yv, z, rstride=10, cstride=10, linewidth = 1)
ax.plot_surface(xv, yv, z, rstride=4, cstride=4, cmap=cm.RdYlBu, linewidth = 0)
plt.show()