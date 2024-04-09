from encrypt import encrypt_data, decrypt_data
import os

def encrypt_file(input_file, output_file):
    # Generate a random key and nonce
    key = os.urandom(32)  # Generate a random key (AES key size is 256 bits)
    nonce = os.urandom(16)  # Generate a random nonce (GCM nonce size is 96 bits)

    # Read content of the target file
    with open(input_file, 'rb') as file:
        payload = file.read()

    # Encrypt the content of the file
    encrypted_payload, tag = encrypt_data(key, nonce, payload)

    # Write encrypted data to the output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_payload)

    return key.encode(), nonce.encode(), tag.encode()

# Example usage:
if __name__ == "__main__":
    input_file = 'input.txt'  # Specify the path to your input file
    output_file = 'encrypted_output.txt'  # Specify the path to your output file

    key, nonce, tag = encrypt_file(input_file, output_file)

    print("Encryption completed:")
    print("Key:", key)
    print("Nonce:", nonce)
    print("Tag:", tag)
