'''

Program computes gamma(t) for t greater or equal to one. 
If t is an integer, program computes (t-1)! directly.
If t is a float, calculates the integral form of the gamma funciton

>>> gamma(5) - 24 < 1e-4
True

>>> gamma(4) - 6 < 1e-4
True

>>> gamma(5./2) - 1.3293403 < 1e-4
True

>>> gamma(7./2) - 3.3233509 < 1e-4
True



'''

from math import *
import numpy
import pdb

total = 0
last_total = 0
dx = 0.01
frac = ''

def h(x):
    return (x**(t-1))*(e**(-x))

def frac_diff():
    if last_total == 0:
        return 'N/A'
    else:
        return abs(total-last_total)/total

def gamma(t):
    if 100 >= t >= 1:
        if type(t) == int:
            return factorial(t-1)
        if type(t) == float:
            frac = 'yes'
            total = 0
            for x in numpy.linspace (0.00000001, 1000, 1001):
                total += (dx/6)*(h(x) +h(x+dx) +4*h((2*x+dx)/2))
                if x == 999:
                    global last_total
                    last_total = total
            return float(total)
    else:
        return 'Please enter a value between 1 and 100.'
    
if __name__ =="__main__":
    t = 5.2
    import doctest
    doctest.testmod()    
    print 'Gamma of',t,'is:',gamma(t)
    if frac == 'yes':
        frac_diff()
