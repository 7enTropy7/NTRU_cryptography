from Polynomial import Zx

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

F = Zx([3,1,4])
G = Zx([0,1])
print(F.print_polynomial())
print(G.print_polynomial())
result = circular_convolution(F,G,3)
print(result.print_polynomial())