class Zx:
    def __init__(self, coeffs):
        self.coeffs = coeffs
   
    def degree(self):
        return len(self.coeffs)-1
   
    def coefficient(self, n):
        if (type(n) != type(1)) or n < 0:
            print('Coefficient does not exist!')
        if n >= len(self.coeffs):
            return 0
        else:
            return self.coeffs[n]

    def print_polynomial(self):
        terms = []
        for i in range(len(self.coeffs)):
            if i == 0:
                terms.append(str(self.coeffs[i]))
            elif i == 1:
                terms.append(str(self.coeffs[i])+"x")
            else:
                terms.append(str(self.coeffs[i])+"x^"+str(i))
        terms.reverse() 
        return "+".join(terms) 

    def eval(self, x):
        result = 0
        for i in range(len(self.coeffs)):
            result += self.coeffs[i]*(x**i)
        return result

    def add(self, other):
        length = max(self.degree(),other.degree()) + 1
        result = [0] * length
        for i in range(len(result)):
            result[i] = self.coefficient(i) + other.coefficient(i)
        
        return Zx(result)

    def multiply_single_term(self, coefficient, degree):
      result = Zx(self.coeffs[:])
      result.coeffs[0:0] = [0]*degree
      for i in range(len(result.coeffs)):
         result.coeffs *= coefficient
      return result

    def multiply(self, other):      
        result = Polynomial([])
        for term in range(other.degree()+1):
            result=result.add(self.multiply_single_term(other.coefficient(term),term))
        return result

F = Zx([3,1,4])
G = Zx([2,7,1])
print(F.print_polynomial())
result = F.multiply_single_term(2,1)
print(result.print_polynomial())