from Polynomial import Zx
from random import randrange

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


#________________________TESTING___________________________

# note that n = len(F.coeffs) = 6
F = Zx([3,1,4,1,5,9])       
G = Zx([2,7,1])

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
