from Polynomial import Zx
from random import randrange
from copy import deepcopy
    
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


#________________________TESTING___________________________

# note that n = len(F.coeffs) = 6
F = Zx([3,1,4,1,5,9])       
G = Zx([2,7,1])

#F = Zx([1,-1,1,1,-1])       
#G = Zx([-1,0,0,0,0,0,0,1])


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

print('Cyclic_Convolution(F,G,n) = ',end='')
result_conv = cyclic_convolution(F,G,3)
print(result_conv.print_polynomial())

print('Balanced Modulus = ',end='')
result_balmod = balancedmod(F,10,3)
print(result_balmod.print_polynomial())

print('Random Polynomial = ',end='')
random_polynomial = Zx([])
random_polynomial.randompoly(5,7)
print(random_polynomial.print_polynomial())
