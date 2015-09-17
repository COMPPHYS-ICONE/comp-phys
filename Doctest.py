#doctest required from HW2 ONWARD
'''

>>> L(1,10000) - 0.69314718056 < 1e-6
True


'''



import pdb
from math import *
from numpy import *

def L(x, n):
    if x <= -1:
        return 'Please enter a value of x greater than negative one!'
    approx = 0
    for i in range(0, n + 1):
        #pdb.set_trace()
        approx += (1./(i+1))*(x/(1.+x))**(i+1) 
        if i == n-1:
            last_approx = approx
    if abs(last_approx-approx)/approx > 1e-6:
        print 'Please increase the value of n for increased accuracy!'
        print 'The error is', (abs(last_approx-approx)/approx)*100, '%'
    return approx

if __name__ =="__main__":
    import doctest
    doctest.testmod()

    x = 10

    

    y = L(x, 100)
    #pdb.set_trace()
    print 'Taylor Series Approximation:', y
    from math import log  #you would guess math module would have log...yes!
    if x > -1:
        exact_val = log(1+x)
        print 'exact_val', exact_val
        from math import log1p  #more accurate for small x.
        print 'log1p output', log1p(x)