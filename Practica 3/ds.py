from Cryptodome.PublicKey import RSA

keyPair = RSA.generate(bits=2048)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha1
hash = int.from_bytes(sha1(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
msg2 = b'A message for signing'
hash = int.from_bytes(sha1(msg2).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)