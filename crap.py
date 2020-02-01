import sympy as sym
from sympy import GF

def make_poly(coeffs):
    """Create a polynomial in x."""
    x = sym.Symbol('x')
    N = len(coeffs)
    coeffs = list(reversed(coeffs))
    y = 0
    for i in range(N):
        y += (x**i)*coeffs[i]
    y = sym.poly(y)
    return y

N = 7
p = 3
q = 41

#-x^4 + x^3 + x^2 - x + 1
f = [-1,1,1,-1,1]

f_poly = make_poly(f)

x = sym.Symbol('x')

Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric=False))
Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric=False))

print('\nf =',f_poly)
print('\nFp =',Fp)
print('\nFq =',Fq)