from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

class Encryptor:
    def __init__(self):
        self.key = get_random_bytes(16)  
        self.iv = get_random_bytes(16)   

    def aes_encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_data = pad(data, AES.block_size)
        return cipher.encrypt(padded_data)

    def sha256_hash(self, data):
        hash_object = SHA256.new()
        hash_object.update(data)
        return hash_object.hexdigest()

# TODO: Implement decryptor class

def file_encryption(method, user_file):
    cryptor = Encryptor()

    with open(user_file, "rb") as file:
        content = file.read()

    if method == "SHA-256":
            return cryptor.sha256_hash(content)
    elif method == "AES":
        return cryptor.aes_encrypt(content)
    else:
        return "Error: method was not found"