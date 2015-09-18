'''

Program computes gamma(t) for t greater or equal to one. 
If t is an integer, program computes (t-1)! directly.
If t is a float, calculates the integral form of the gamma funciton

>>> abs(abs(gamma(5)) - 24) < 1e-4
True

>>> abs(abs(gamma(4)) - 6) < 1e-4
True

>>> abs(abs(gamma(5./2)[0]) - 1.3293403) < 1e-4
True

>>> abs(abs(gamma(7./2)[0]) - 3.3233509) < 1e-4
True

    Call signature  :
    
    python gamma.py -t 9.784 -tol .001 
    
    To run doctests in verbose mode:
    
    python -m doctest -v gamma.py

'''

from math import *
import numpy
import pdb

steps = 100

def h(x,t):
    return (x**(t-1))*(e**(-x))

def frac_diff():
    if last_total == 0:
        return 'N/A'
    else:
        return abs(total-last_total)/total

def gamma(t,tol = 1e-4):
    if 100 >= t >= 1:
        if type(t) == int:
            return factorial(t-1)
        if type(t) == float:
            steps = 100
            dx = 1.
            total = 0
            last_total = 0
            fractional_diff = 1000
            #pdb.set_trace()
            while fractional_diff > tol:
                last_total = total
                total = 0
                for x in numpy.linspace (0.0000000001, 100, steps+1):
                    total += (dx/6)*(h(x,t) +h(x+dx,t) +4*h((2*x+dx)/2,t))
                fractional_diff = abs(total-last_total)/total
                steps *=2
                dx /=2
            return float(total), last_total, fractional_diff
    else:
        return 'Please enter a value between 1 and 100.'
    


    
if __name__ =="__main__":
    frac = ''
    fractional_diff = 0
    total = 0
    last_total = 0
    import argparse
    import doctest
    #doctest.testmod()
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', type = float)
    parser.add_argument('-tol', type = float)
    args = parser.parse_args()
    t = args.t
    tol = args.tol

    stringofT = str(t)
    
    if stringofT[-1] == '0':
        t = int(t)
        
    
    
    if type(t) == int:
        fact = gamma(t,tol)
        print 'Gamma of',t,'is:',fact
    if type(t) == float:
        total, last_total, fractional_diff = gamma(t,tol)
        print 'Gamma of',t,'is:',total
        print 'frac_diff =', "{:0.7f}".format(fractional_diff*100),"%"

