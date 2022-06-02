from Cryptodome.Cipher import DES
key = b'holacomo'
op = int(input('Ingresa operacion (encrypt 0, decrypt 1)\n>'))
if op == 0:
	cipher = DES.new(key, DES.MODE_OFB)
	image = open("thundercats.bmp","rb")
	new_image = open("thunder_OFB.bmp","wb")
	new_file = open("iv.txt","wb")
	new_image.write(image.read(54))
	bytes_to_encrypt = image.read()
	new_file.write(cipher.iv)
	new_image.write(cipher.encrypt(bytes_to_encrypt))
