from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Function to encrypt data using AES-GCM
def encrypt_data(key, nonce, data, associated_data=b""):
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    encryptor.authenticate_additional_data(associated_data)
    ciphertext = encryptor.update(data) + encryptor.finalize()
    tag = encryptor.tag
    return ciphertext, tag

# Function to decrypt data using AES-GCM
def decrypt_data(key, nonce, ciphertext, tag, associated_data=b""):
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    decryptor.authenticate_additional_data(associated_data)
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext