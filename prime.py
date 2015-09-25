'''

HW03
Ian Cone
Partner: Ritesh Pakala

This function finds all prime numbers between 2 given integers. 
Given integers are entered via command line, and then all prime
numbers in between are printed


>>> find_primes(0,10) == [2, 3, 5, 7]
True

>>> find_primes(0,15) == [2, 3, 5, 7, 11, 13]
True

>>> find_primes(16,32) == [17, 19, 23, 29, 31]
True

>>> find_primes(37,44) == [37, 41, 43]
True



Call signature  :

    python prime.py -a 9 -b 27 
    
    To run doctests in verbose mode:
    
    python -m doctest -v prime.py
    
    
'''
import numpy as np
prime_list = []
divis_by = 0

def find_primes(a,b):
    prime_list = []
    while a <= b:
        divis_by = 0
        for j in np.arange(1,a+1):
            if a % j == 0:
                divis_by += 1
        if divis_by == 2:
            prime_list.append(a)
        a += 1
    return prime_list
    
    
    
    
if __name__ == "__main__":
    import doctest
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type = int)
    parser.add_argument('-b', type = int)
    args = parser.parse_args()
    a = args.a
    b = args.b
    print 'The primes between',a,'and',b,'are:',find_primes(a,b)
    