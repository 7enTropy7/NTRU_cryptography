import math
from random import randint
import numpy as np
#import matplotlib.pyplot as plt

def sq_root_mod_n(n, p):   
    n = n%p 
    for x in range (2, p): 
        if ((x*x)%p == n):  
            return x
    return 0 

plainText = input("Enter Message: ")

print('Curve Parameters')
elliptic_a = int(input("Enter A: "))
elliptic_b = int(input("Enter B: "))

ord_lst = [ord(ch) for ch in plainText]
k=20 
p=751

x_coords = []
y_coords = []
encoded_points = []

for m in ord_lst:
    for j in range(1,k):
        x_m = m*k+j
        n = pow(x_m,3) + elliptic_a * x_m + elliptic_b
        y_m = sq_root_mod_n(n,p)
        if (y_m != 0):
            x_coords.append(x_m)
            y_coords.append(y_m)
            encoded_points.append((x_m,y_m))
            break

print('Encoded points generated: ')
for i in range(len(x_coords)):
    print('{},{}'.format(x_coords[i],y_coords[i])) 

    

decoded_Msg = []
for x,y in encoded_points:
    d = math.floor((x-1)/k)
    decoded_Msg.append(chr(d))

print('\nDecoded Message: ',end='')
print(''.join(decoded_Msg))

#plt.plot(x_coords,y_coords,'s')
#plt.show()

def pyth(x,y):
  return x**2+y**2

decoded_points = []
def primitive_start_point(N):
  for i in range(-math.ceil(math.sqrt(N)),math.ceil(math.sqrt(N))):
    for j in range(-math.ceil(math.sqrt(N)),math.ceil(math.sqrt(N))):
      if i**2+j**2==N:
        decoded_points.append([j,i])

  return decoded_points

def cantor_pair(k1, k2, safe=True):
    z = int(0.5 * (k1 + k2) * (k1 + k2 + 1) + k2)
    if safe and (k1, k2) != cantor_unpair(z):
        raise ValueError("{} and {} cannot be paired".format(k1, k2))
    return z


def cantor_unpair(z):
    w = np.floor((np.sqrt(8 * z + 1) - 1) / 2)
    t = (w**2 + w) / 2
    y = int(z - t)
    x = int(w - y)
    # assert z != pair(x, y, safe=False):
    return x, y


def dec_ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return nums[::-1]

print(dec_ternary(11))

def ternary_dec(t):
    n = 0
    t = t[::-1]
    for i in range(len(t)):
        n += (3**i)*t[i]
    return n

print(ternary_dec([1,0,2]))

for i in range(len(encoded_points)):
    x = x_coords[i]
    y = y_coords[i]
    print(dec_ternary(cantor_pair(x,y)))