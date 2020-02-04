import math
from random import randint
from Polynomial import Zx

def sq_root_mod_n(n, p):   
    n = n%p 
    for x in range (2, p): 
        if ((x*x)%p == n):  
            return x
    return 0 

def pyth(x,y):
    return x**2+y**2

def primitive_start_point(N):
    for i in range(math.ceil(math.sqrt(N))):
        for j in range(math.ceil(math.sqrt(N))):
            if i**2+j**2==N:
                return (j,i)

def dec_ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(r)
    return nums[::-1]

def introduce_negative_one(lst):
    for i in range(len(lst)):
        if lst[i] == 2:
            lst[i] = -1
    return lst

def revert_introduce_negative_one(lst):
    for i in range(len(lst)):
        if lst[i] == -1:
            lst[i] = 2
    return lst


def ternary_dec(t):
    n = 0
    t = t[::-1]
    for i in range(len(t)):
        n += (3**i)*t[i]
    return n

def padder(lst,N):
    while len(lst)!=N:
        lst.insert(0,0)
    return lst


def koblitz_encoder(plainText,elliptic_a,elliptic_b):
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
    encoded_message = []
    #print('koblitz encoding:')
    for i in range(len(encoded_points)):
        x = x_coords[i]
        y = y_coords[i]
        encoded_message.append(dec_ternary(pyth(x,y)))
        #print(x,y)
    n = 0
    for i in encoded_message:
        if len(i)>=n:
            n = len(i)
        for j in range(len(i)):
            i[j] = int(i[j])
    ntru_input = []
    for element in encoded_message:
        ntru_input.append(Zx(padder(introduce_negative_one(element),n)))
    return ntru_input,n

def points_decoder(lst):
    decoded = []
    for element in lst:
        decoded.append(primitive_start_point(ternary_dec(revert_introduce_negative_one(element))))
    return decoded

def koblitz_decoder(encoded_points):
    k = 20
    decoded_Msg = []
    for x,y in encoded_points:
        d = math.floor((x-1)/k)
        decoded_Msg.append(chr(d))
    decoded_message = ''.join(decoded_Msg)
    return decoded_message