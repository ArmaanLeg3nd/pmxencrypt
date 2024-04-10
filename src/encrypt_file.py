from src.algorithm import encrypt_data
def encrypt_file(key, nonce, input_file):

    # Read content of the target file
    with open(input_file, 'rb') as file:
        payload = file.read()

    # Encrypt the content of the file
    encrypted_payload, tag = encrypt_data(key, nonce, payload)

    return encrypted_payload, tag