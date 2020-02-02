from Polynomial import Zx
from random import randrange
from copy import deepcopy
import sympy as sym
from sympy import GF
import math

def cyclic_convolution(F,G,n):
    result = F.multiply(G)
    t = Zx([])
    t.coeffs = [0]*n
    for i in range(result.degree()+1):
        t.coeffs[i%n] += result.coeffs[i]    
    return t

def balancedmod(F,q,n):     # n is the no. of coeff in F
    result = Zx([])
    for i in range(n):
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
    g = invertmodprime(F,N,2)
    while True:
        r = balancedmod(cyclic_convolution(F,g,N),q,N)
        flag = 0
        for i in range(1,len(r.coeffs)):
            if r.coeffs[i]!=0:
                flag =1 
                break 
        if r.coeffs[0] == 1 and flag == 0: 
            break
        e = Zx([2])
        l = e.add(r.multiply_single_term(-1,0))
        g = balancedmod(cyclic_convolution(g,l,N),q,N)
    return g

#________________________TESTING___________________________

F = Zx([1,-1,1,1,-1])
G = Zx([1,0,1])       

N = 7
p = 3
q = 256

print('F = ',end='')
print(F.print_polynomial())
print('G = ',end='')
print(G.print_polynomial())

print('F + G = ',end='')
result_addition = F.add(G)
print(result_addition.print_polynomial())

print('F * G = ',end='')
result_multiply = F.multiply(G)
print(result_multiply.print_polynomial())

print('F / G = ',end='')
X = deepcopy(F)
Y = deepcopy(G)
quotient, remainder = poly_divmod(X, Y)
print("Quotient: {}, Remainder: {}\n".format(quotient.print_polynomial(), remainder.print_polynomial()))

print('Invert_polynomial(F,N,p) = ',end='')
Fp = invertmodprime(F,N,p)
print(Fp.print_polynomial())


print('invertmodpowerof2(F,N,q) = ',end='')
Fq = invertmodpowerof2(F,N,q)
print(cyclic_convolution(F,Fq,N).print_polynomial())

print('Cyclic_Convolution(F,G,n) = ',end='')
result_conv = cyclic_convolution(F,G,7)
print(result_conv.print_polynomial())

print('Balanced Modulus = ',end='')
result_balmod = balancedmod(F,10,3)
print(result_balmod.print_polynomial())

print('Random Polynomial = ',end='')
random_polynomial = Zx([])
random_polynomial.randompoly(5,7)
print(random_polynomial.print_polynomial())
