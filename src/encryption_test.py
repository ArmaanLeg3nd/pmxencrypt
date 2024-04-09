from encrypt import encrypt_data, decrypt_data
import os

def main():
    key = os.urandom(32)  # Generate a random key (AES key size is 256 bits)
    nonce = os.urandom(16)  # Generate a random nonce (GCM nonce size is 96 bits)
    payload = b'''a=6
b=7
print(a+b)'''
    
    encrypted_payload, tag = encrypt_data(key, nonce, payload)
    decrypted_payload = decrypt_data(key, nonce, encrypted_payload, tag)
    print(key)
    print(tag)
    print(nonce)
    print(encrypted_payload)
    
    print("Original Payload:", payload)
    print("Encrypted Payload:", encrypted_payload)
    print("Decrypted Payload:", decrypted_payload.decode('utf-8'))
    exec(decrypted_payload)


if __name__ == "__main__":
    main()
