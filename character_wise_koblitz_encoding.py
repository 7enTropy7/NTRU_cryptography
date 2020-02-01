import math
from random import randint
import matplotlib.pyplot as plt

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

plt.plot(x_coords,y_coords,'s')
plt.show()