from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import sys

def decrypt(password, filename):
    in_file = open(filename, 'rb')
    encrypted_message = in_file.read()
    in_file.close()

    key = SHA256.new(password.encode('utf-8')).digest()
    iv = encrypted_message[16:32]
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return cipher.decrypt(encrypted_message[32:]).decode('utf-8')
    
print(decrypt(sys.argv[2], sys.argv[1]))

# python this.py filename password