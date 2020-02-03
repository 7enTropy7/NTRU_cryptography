from NtruEncrypt import *
from Polynomial import Zx

N = 7
d = 5
p = 3
q = 256

public_key,private_key = generate_keypair(p,q,d,N)

print('Public Key = ',end='')
print(public_key.print_polynomial())

print('Message = ',end='')              #-x^6 - x^4 + x^2 + 1
plain_text = Zx([1,0,1,0,-1,0,-1])
print(plain_text.print_polynomial())

print('Encrypted = ',end='')
cipher_text = encrypt(plain_text,public_key,d,N,q)
print(cipher_text.print_polynomial())

print('Decrypted = ',end='')
decrypted_message = decrypt(cipher_text,private_key,p,q,N)
print(decrypted_message.print_polynomial())

cross_check(decrypted_message,plain_text)