from Polynomial import Zx

F = Zx([3,1,4])
G = Zx([2,7,1])
print(F.print_polynomial())
print(G.print_polynomial())
result = F.multiply(G)
print(result.print_polynomial())