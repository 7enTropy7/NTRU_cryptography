'''

def extendedEuclideanGF2(a, b): # extended euclidean. a,b are values 10110011... in         integer form
    inita, initb = a, b   # if a and b are given as base-10 ints
    x, prevx = 0, 1
    y, prevy = 1, 0
    while b != 0:
        q = a//b
        a, b = b, a%b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
    print("Euclidean  %d * %d + %d * %d = %d" % (inita, prevx, initb, prevy, a))
    i2b = lambda n: int("{0:b}".format(n))  # convert decimal number to a binary value in a decimal number
    return i2b(a), i2b(prevx), i2b(prevy)  # returns gcd of (a,b), and factors s and t




#==================================================================================

EPSILON = 0.0001

# Recursively calculates the gcd of two polynomials in given finite field p (for prime p)
# Polynomials are given by a list of coefficients from largest to smallest.
# When p=0 tries to calculate the gcd in R, percision makes this difficult, and is not reliable.
def gcd(f, g, p=0, verbose=False):
    if (len(f)<len(g)):
        return gcd(g,f,p, verbose)
    
    r = [0]*len(f)
    r_mult = reciprocal(g[0], p)*f[0]
    
    for i in range(len(f)):
        if (i < len(g)):
            r[i] = f[i] - g[i]*r_mult
        else:
            r[i] = f[i]
        if (p != 0):
            r[i] %= p
   
    if(verbose):
        print(f,'by',g,'got',r)
        
    while (abs(r[0])<EPSILON):
        r.pop(0)
        if (len(r) == 0):
            return g
    
    return gcd(r, g, p, verbose)
    
# returns reciprocal of n in finite field of prime p, if p=0 returns 1/n#
def reciprocal(n, p=0):
    if (p == 0):
        return 1/n
    for i in range(p):
        if (n*i)%p == 1:
            return i
    return None
       
f = [1,0,0,0,0,-1]
g = [1,0,1]

print(gcd(f,g,5, True))

# x^6 + 2*x^4 + x
# [0,1,0,0,2,0,1]
#print(reciprocal(12, 19))

#===================================================================================

import numpy as np

def gf2_xgcd(b, a):
    """Perform Extended Euclidean Algorithm over GF2

    Given polynomials ``b`` and ``a`` in ``GF(p)[x]``, computes polynomials
    ``s``, ``t`` and ``h``, such that ``h = gcd(f, g)`` and ``s*b + t*a = h``.
    The typical application of EEA is solving polynomial diophantine equations and findining multiplicative inverse.


    Parameters
    ----------
    b : ndarray (uint8 or bool) or list
        b polynomial's coefficients.
    a : ndarray (uint8 or bool) or list
        a polynomial's coefficients.
    Returns
    -------
    y2 : ndarray of uint8
        s polynomial's coefficients.
    x2 : ndarray of uint8
        t polynomial's coefficients.
    b : ndarray of uint8
        h polynomial's coefficients.

    Notes
    -----
    Rightmost element in the arrays is the leading coefficient of the polynomial.
    In other words, the ordering for the coefficients of the polynomials is like the one used in MATLAB while
    in Sympy, for example, the leftmost element is the leading coefficient.

    Examples
    ========

    >>> x = np.array([1, 1, 1, 1, 1, 0, 1, 0, 1], dtype="uint8")
    >>> y = np.array([1, 0, 1], dtype="uint8")
    >>> gf2_xgcd(x,y)
    (array([0, 1, 1, 1], dtype=uint8),
    array([1, 1], dtype=uint8),
    array([1], dtype=uint8))

    """

    x1 = np.array([1], dtype="uint8")
    y0 = np.array([1], dtype="uint8")

    x0 = np.array([], dtype="uint8")
    y1 = np.array([], dtype="uint8")

    while True:

        q, r = gf2_div(b, a)

        b = a

        if not r.any():
            break

        a = r

        if not (q.any() and x1.any()):  # if q is zero or x1 is zero
            x2 = x0
        elif not x0.any():  # if x0 is zero
            x2 = mul(x1, q)
        else:
            mulres = mul(x1, q)

            x2 = gf2_add(x0, mulres)

        if not (q.any() and y1.any()):
            y2 = y0
        elif not y0.any():
            y2 = mul(y1, q)
        else:
            mulres = mul(y1, q)

            y2 = gf2_add(y0, mulres)

        # update
        y0 = y1
        x0 = x1
        y1 = y2
        x1 = x2

    return y2, x2, b

x = np.array([1,-1,1,1,-1], dtype="uint8")
y = np.array([-1,0,0,0,0,0,0,1], dtype="uint8")
print(gf2_xgcd(x,y))

'''

#=====================================================================================


# Finding the inverse of (x^2 + 1) modulo (x^4 + x + 1) using Extended Euclidean Algorithm in SageMath [GF(2^4)]
# By: Ngangbam Indrason

# Enter the coefficients of modulo n polynomial in a list from lower power to higher power
# Eg.: x^4 + x + 1 => 1.x^0 + 1.x^1 + 0.x^2 + 0.x^3 + 1.x^4
r1 = [-1,0,0,0,0,0,0,1]

# Enter the coefficients of polynomial to find inverse in a list from lower power to higher power
# Eg.: x^2 + 1 => 1.x^0 + 0.x^1 + 1.x^2
r2 = [1,-1,1,1,-1]

# Creating a copy of r1 and r2 in a and b respectively
a = list(r1)
b = list(r2)
itr = 1

def mod(a,b):
    return a%b

# Function to find degree of the polynimial
def getDegree(a):
    global deg
    for i in range(len(a)):
        if a[i] != 0:
            deg = i
    return deg

# Function to perform polynomial division: a1 = Dividend, b1 = Divisor
def doDivision(a1,b1):
    
    # Initialize quotient list with 0s of size as r1
    qq = [0]*len(r1)
    
    ai = getDegree(a1)
    bj = getDegree(b1)    
    
    while ai >= bj and 1 in a1:
        t_pow = ai-bj
        t_coeff = a1[ai]/b1[bj]
        
        qq[t_pow] = t_coeff
        
        # Initializing temporary list for intermediate products
        t_mul = [0]*len(r1)
        
        # Multipliying divisor with quotient
        for i in range(bj+1):
            t_mul[i+t_pow] = b1[i]*t_coeff
            
        # New intermediate dividend
        for i in range(len(a1)):
            a1[i] = mod(a1[i] - t_mul[i],2)
                 
        ai = getDegree(a1)
    
    return qq, a1

# Initialize t1 list as 0
t1 = [0]*len(r1)

# Initialize t2 list as 1
t2 = [0]*len(r1)
t2[0] = 1

# Initialize t list as 0
t = [0]*len(r1)

# Extended Euclidean Algorithm
while 1 in b:
    print('\n'+str(itr))
    print('Dividend: '+str(a))
    print('Divisor: '+str(b))
    quot, rem = doDivision(a,b)
    print('\nQuotient: '+str(quot))
    print('Remainder: '+str(rem))
    
    #Initializing intermediate list for quotient * t2
    t_qt2 = [0]*len(r1)
    d_quot = getDegree(quot)
    d_t2 = getDegree(t2)
    
    # Multipliying quotient and t2
    for i in range(d_quot+1):
        for j in range(d_t2+1):
            t_qt2[i+j] = t_qt2[i+j] + (quot[i] * t2[j])
        

    # Calculating t = t1 - quotient * t2
    for i in range(len(r1)):
        t[i] = mod(t1[i] - t_qt2[i],2)
    
    # Checking the degree of t: if deg(t) == deg(r1), then perform t = t modulo r1
    if getDegree(r1) == getDegree(t):
        print('\nt needs to perform modulo n')
        print('t_value before modulo: '+str(t))
        t_quo, t_rem = doDivision(t,r1)
        t = list(t_rem)
        
    
    print('\nt1: '+str(t1))
    print('t2: '+str(t2))
    print('t: '+str(t))
    a = list(b)
    b = list(rem)
    t1 = list(t2)
    t2 = list(t)

    itr = itr+1
    
# The result can be generated by rearranging the cofficients in the list from lower power to higher power    
print('\nInverse of the polynomial: '+str(t1))