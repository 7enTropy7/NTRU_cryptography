from Polynomial import Zx
from random import randrange
from copy import deepcopy
import sympy as sym
from sympy import GF
import math
import functools

def cyclic_convolution(F,G,n):
    result = F.multiply(G)
    t = Zx([])
    t.coeffs = [0]*n
    for i in range(result.degree()+1):
        t.coeffs[i%n] += result.coeffs[i]    
    return t

def balancedmodulus(F,q,N):     
    result = Zx([])
    for i in range(N):
        result.coeffs.append(((F.coeffs[i] + q//2) % q) - q//2)
    return result

def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def poly_divmod(X, Y):
    num = X.coeffs[:]
    normalize(num)
    den = Y.coeffs[:]
    normalize(den)

    if len(num) >= len(den):
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shiftlen + 1):
        mult = num[-1] / divisor
        quot = [mult] + quot
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]
        num.pop()
        den.pop(0)
    normalize(num)
    quotient = Zx([])
    remainder = Zx([])
    quotient.coeffs = quot[:]
    remainder.coeffs = num[:]
    return quotient, remainder

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def make_poly(coeffs):
    x = sym.Symbol('x')
    n = len(coeffs)
    coeffs = list(reversed(coeffs))
    y = 0
    for i in range(n):
        y += (x**i)*coeffs[i]
    y = sym.poly(y)
    return y

def invertmodprime(F,N,p):
    Fp = Zx([])
    f = F.coeffs[::-1]
    f_poly = make_poly(f)
    x = sym.Symbol('x')
    t = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric=False))
    Fp.coeffs = t.all_coeffs()[::-1]
    return Fp

def Log2(x): 
    if x == 0: 
        return False 
    return (math.log10(x)/math.log10(2)) 
  
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 

def invertmodpowerof2(F,N,q):
    g = Zx([])
    if isPowerOfTwo(q) == False:
        print('q has to be a power of 2') 
        return None
    g = invertmodprime(F,N,2)
    while True:
        r = balancedmodulus(cyclic_convolution(F,g,N),q,N)
        flag = 0
        for i in range(1,len(r.coeffs)):
            if r.coeffs[i]!=0:
                flag =1 
                break 
        if r.coeffs[0] == 1 and flag == 0: 
            break
        e = Zx([2])
        l = e.add(r.multiply_single_term(-1,0))
        g = balancedmodulus(cyclic_convolution(g,l,N),q,N)
    return g

def generate_keypair(p,q,d,N):
    while True:
        try:
            F = Zx([])
            F.randompoly(d,N)

            F_inverse = invertmodprime(F,N,p)
            Fq = invertmodpowerof2(F,N,q)
            break
        except:
            pass

    g = Zx([])
    g.randompoly(d,N)
    r = Zx([p])
    t = cyclic_convolution(Fq,g,N).multiply(r)
    public_key = balancedmodulus(t,q,N)
    secret_key = F,F_inverse
    return public_key,secret_key    

def encrypt(message,public_key,d,N,q):
    r = Zx([])
    r.randompoly(d,N)           # r is the binding value
    cipher_text = balancedmodulus(cyclic_convolution(public_key,r,N).add(message),q,N)
    return cipher_text

def decrypt(cipher_text,private_key,p,q,N):
    F, F_inverse = private_key
    a = balancedmodulus(cyclic_convolution(cipher_text,F,N),q,N)
    decrypted_message = balancedmodulus(cyclic_convolution(a,F_inverse,N),p,N)
    return decrypted_message

def cross_check(decrypted_message,plain_text):
    if functools.reduce(lambda i,j:i and j,map(lambda m,k:m == k,plain_text.coeffs,decrypted_message.coeffs),True):
        print ("Successful!") 
    else : 
        print ("Error!!!") 