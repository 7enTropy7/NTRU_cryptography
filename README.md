[![python3](https://img.shields.io/badge/python3-v3.6-green?style=for-the-badge&logo=python)](https://www.python.org)

[![Linkedin](https://img.shields.io/badge/Linkedin-Unnikrishnan%20Menon-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/unnikrishnan-menon-aa013415a/) [![Linkedin](https://img.shields.io/badge/Linkedin-Awnon%20Bhowmik-red?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/awnon-bhowmik-13a5a013b/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACIUlr4BQG5MmK7AYfJbU5Zaacunw1qLanM)

[![GitHub followers](https://img.shields.io/github/followers/7enTropy7?label=Follow&style=social)](https://github.com/7enTropy7?tab=followers) [![GitHub stars](https://img.shields.io/github/stars/7enTropy7/NTRU_cryptography.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/7enTropy7/NTRU_cryptography/stargazers/)

# NTRU_cryptography
A Post-Quantum Encryption Algorithm

Created in collaboration with [Awnon Bhowmik](https://github.com/awnonbhowmik)

NTRU is an open-source public key cryptosystem that uses
lattice-based cryptography to encrypt and decrypt data. Unlike
other popular public-key cryptosystems, it is resistant to
attacks using Shor's Algorithm and its performance has been
shown to be significantly greater. 

This paper talks about how
Koblitz encoding from Elliptic Curve Cryptography (ECC)
can be used to convert each character in a dataset to a point on
an elliptic curve. A sum of squares analogy is pitted against
the cantor pairing function to turn the point to a single
number, which is converted to a sequence of coefficients in Z.
A polynomial is then generated for each of these characters.
Then the polynomial is reduced, and then shown that choosing
appropriate parameters for the cryptosystem can make it
highly secure and that the decryption algorithm turns out
taking linear time. Since each character is represented by its
own polynomial, it increases obscurity thereby increasing the
complexity for decryption and thus the security level. 

A form
of data compression has also been implemented and it has
been tested whether data compression and expansion during
the encryption-decryption process results in original data with
no or minimal loss.

## Cloning
```bash
$ git clone https://github.com/7enTropy7/NTRU_cryptography.git
```

## Dependencies
```bash
$ pip3 install -r requirements.txt
```

## Demonstration

![ntru_gif](https://user-images.githubusercontent.com/36446402/82535268-40895b80-9b64-11ea-81cc-0c55677fc22a.gif)

## Output

![Screenshot from 2020-02-06 12-43-24](https://user-images.githubusercontent.com/36446402/73914025-5d17c580-48de-11ea-8ae5-b07e0940b306.png)


## Authors
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Unnikrishnan-teal.svg)](https://www.linkedin.com/in/unnikrishnan-menon-aa013415a/) [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Awnon-green.svg)](https://www.linkedin.com/in/awnon-bhowmik-13a5a013b/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACIUlr4BQG5MmK7AYfJbU5Zaacunw1qLanM)
* [**Awnon Bhowmik**](https://github.com/awnonbhowmik)
* [**Unnikrishnan Menon**](https://github.com/7enTropy7)

<!-- [![Github](https://img.shields.io/badge/Github-Unnikrishnan%20Menon-blue?style=for-the-badge&logo=github)](https://github.com/7enTropy7)

[![Github](https://img.shields.io/badge/Github-Awnon%20Bhowmik-green?style=for-the-badge&logo=github)](https://github.com/awnonbhowmik) -->

## Citation
If you find this code useful in your research, please consider citing:

