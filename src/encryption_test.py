from encrypt import encrypt_data, decrypt_data
import os

def main():
    key = os.urandom(32)  # Generate a random key (ChaCha20 key size is 256 bits)
    nonce = os.urandom(16)  # Generate a random nonce (ChaCha20 nonce size is 96 bits)

    payload = b'This is a test payload.'  # Example payload
    
    encrypted_payload = encrypt_data(key, nonce, payload)
    decrypted_payload = decrypt_data(key, nonce, encrypted_payload)
    
    print("Original Payload:", payload)
    print("Encrypted Payload:", encrypted_payload)
    print("Decrypted Payload:", decrypted_payload.decode('utf-8'))

if __name__ == "__main__":
    main()
