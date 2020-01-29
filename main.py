from Polynomial import Zx
from random import randrange

def circular_convolution(F,G,n): 
    result = F.multiply(G)
    t_ = []
    for i in range(len(result.coeffs)):
        if i>=n:
            t_.append(result.coeffs[i])

    result.coeffs = result.coeffs[0:3]

    if len(result.coeffs)>len(t_):
        for i in range(len(t_)):
            result.coeffs[i]+=t_[i]
    else:
        for i in range(len(result.coeffs)):
            result.coeffs[i]+=t_[i]
    
    return result

def balancedmod(F,q,n):     # n is the no. of coeff in F
    result = Zx([])
    for i in range(n):
        result.coeffs.append(((F.coeffs[i] + q//2) % q) - q//2)
    return result



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

print('Circular_Convolution(F,G) = ',end='')
result_conv = circular_convolution(F,G,3)
print(result_conv.print_polynomial())

print('Balanced Modulus = ',end='')
result_balmod = balancedmod(F,10,3)
print(result_balmod.print_polynomial())

print('Random Polynomial = ',end='')
random_polynomial = Zx([])
random_polynomial.randompoly(5,7)
print(random_polynomial.print_polynomial())
