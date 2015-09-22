#%matplotlib 
'''

HW03
Ian Cone
Partner: Ritesh Pakala

This function models the wavefunction of two fermions of 
opposite spin and then plots the wavefunction and probablility 
density. x1 and x2 are inputted by the user at the command prompt

   
Call signature  :

    python gamma.py -t 9.784 -tol .001 
    
    To run doctests in verbose mode:
    
    python -m doctest -v gamma.py
    
    
'''

def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
    psi = (2/a)*((np.sin(n1*np.pi*x1/a)*np.sin(n2*np.pi*x1/a)) - (np.sin(n1*np.pi*x2/a)*np.sin(n2*np.pi*x1/a)))
    return psi, (psi**2)
    
if __name__ == "__main__":
    import doctest
    import argparse
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-x1', type = float)
    parser.add_argument('-x2', type = float)
    args = parser.parse_args()
    x1 = args.x1
    x2 = args.x2
    
     
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm
    
    
    fig = plt.figure()
    plt.title('Antisymmetric Spatial Wave Function')
    ax = fig.add_subplot(121, projection = '3d')
    x = y = np.linspace(-x1,x2,100)
    xv, yv = np.meshgrid(x,y)
    wave_f, prob_dens = antisym(xv,yv,n1 = 1, n2 = 2, a = 1.0)#2 rows, 1 column, first of the two
    #ax.plot_wireframe(xv, yv, z, rstride=1, cstride=1, linewidth = 1)
    ax.plot_surface(xv, yv, wave_f, rstride=3, cstride=3, cmap=cm.Paired, linewidth = 0)
    fig.subplots_adjust(top=0.85) # without this, won't be able to see plot title(moves plot down a little bit)
    plt.suptitle('Wave Function')

    #plt.plot(x, y1, 'r.', lw = 2)
    #plt.grid(True)
    ax.set_ylabel('y1')

    bx = plt.subplot(122, projection ='3d')# 2 rows, 1 column, second of two       #both ways are perfectly legal
    #ax.plot_wireframe(xv, yv, z, rstride=10, cstride=10, linewidth = 1)
    bx.plot_surface(xv, yv, prob_dens, rstride=3, cstride=3, cmap=cm.Paired, linewidth = 0)
    fig.subplots_adjust(top=0.85)
    plt.suptitle('Probability Density')
    
    #plt.xlabel('x')
    #plt.ylabel('y2')

    plt.show()
    
