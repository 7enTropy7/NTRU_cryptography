from NtruEncrypt import *
from Polynomial import Zx
from num_to_polynomial import *

d = 5
p = 3
q = 128

message = input("Enter Message: ")

print('Curve Parameters')
elliptic_a = int(input("Enter A: "))
elliptic_b = int(input("Enter B: "))

character_polynomials,N = koblitz_encoder(message,elliptic_a,elliptic_b) 

public_key,private_key = generate_keypair(p,q,d,N)

print('\nPublic Key = ',end='')
print(public_key.print_polynomial())

print('\nEncrypted = ')
cipher_polys = []
for element in character_polynomials:
    cipher_text = encrypt(element,public_key,d,N,q)
    cipher_polys.append(cipher_text)
    print(cipher_text.print_polynomial())

print('\nDecrypted = ',end='')
dec_w = []
for element in cipher_polys:
    decrypted_message = decrypt(element,private_key,p,q,N)
    #print(decrypted_message.print_polynomial())
    dec_w.append(decrypted_message.coeffs)
decrypted_plain_text = koblitz_decoder(points_decoder(dec_w))
print(decrypted_plain_text)