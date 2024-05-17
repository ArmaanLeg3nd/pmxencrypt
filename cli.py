from src.combiner import combine
from src.encrypt_file import encrypt_file
import os
import time
import threading
from pyfiglet import Figlet

def getinputfilepath():
    input_file_path = input("Enter the path of the malware file you want to encrypt >>> ")
    return input_file_path

def getoutputfilepath():
    output_path = input("Enter the encrypted file destination path >>> ")
    return output_path

def getoutputfilename():
    output_file_name = input("Enter the name of the destination file >>> ")
    return output_file_name

def loading_dots(interval=1):
    print("\nEncrypting malware file.", end='')
    try:
        while not stop_loading_event.is_set():
            print('.', end='', flush=True)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nProgram interrupted... Exiting...")

def ascii_art():
    print("\n\n")
    ascii = Figlet(font='slant_relief',width=200)
    print(ascii.renderText('PMXencrypt'))
    print("\n\n")
    
        
def process_files(input_file_path, output_path):
    # Start the loading indicator in a separate thread
    loading_thread = threading.Thread(target=loading_dots)
    loading_thread.start()
    e=False
    
    try:
        key = os.urandom(32)  # Generate a random key (AES key size is 256 bits)
        nonce = os.urandom(16)  # Generate a random nonce (GCM nonce size is 96 bits)
        payload, tag = encrypt_file(key, nonce, input_file_path) # Encrypt the malware and return the encrypted payload and tag
        combine(key, nonce, tag, payload, output_path) # Combine the encrypted payload with the decryption function and write to a new file which is executable from the get go
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted... Exiting...")
        e=True
    
    finally:
        if(e==False):
            print("\n\nEncryption complete!")
            # Signal the loading thread to stop and wait for it to finish
        stop_loading_event.set()
        loading_thread.join()

ascii_art()
input_file_path = getinputfilepath()
output_path = getoutputfilepath()
output_file_name = getoutputfilename()
if not output_file_name.endswith(".py"):
    output_file_name += ".py"
output_path = output_path + "/" + output_file_name
stop_loading_event = threading.Event() # Initialize the stop event
process_files(input_file_path, output_path)