import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
from src.combiner import combine
from src.encrypt_file import encrypt_file
import os
import threading

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_path():
    output_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def open_output_folder(output_path):
    if os.path.isdir(output_path):
        os.startfile(output_path)

def process_files():
    input_file_path = input_file_entry.get()
    output_path = output_path_entry.get()
    output_file_name = output_file_name_entry.get()
    if not output_file_name.endswith(".py"):
        output_file_name += ".py"
    output_path_full = os.path.join(output_path, output_file_name)
    key = os.urandom(32)  # Generate a random key (AES key size is 256 bits)
    nonce = os.urandom(16)  # Generate a random nonce (GCM nonce size is 96 bits)
    payload, tag = encrypt_file(key, nonce, input_file_path) # Encrypt the file and return the encrypted payload and tag
    combine(key, nonce, tag, payload, output_path_full) # Combine the encrypted payload with the decryption function and write to a new file
    loading_window.destroy()
    show_completion_message(output_path)

def start_processing():
    global loading_window
    loading_window = tk.Toplevel(window)
    loading_window.title("Processing")
    loading_window.geometry("300x100")
    loading_window.resizable(False, False)
    ttk.Label(loading_window, text="Processing...").pack(pady=10)
    progress = ttk.Progressbar(loading_window, mode="indeterminate")
    progress.pack(pady=10)
    progress.start()

    # Start the file processing in a new thread
    thread = threading.Thread(target=process_files)
    thread.start()

def show_completion_message(output_path):
    completion_window = tk.Toplevel(window)
    completion_window.title("Encryption Completed!")
    completion_window.geometry("300x100")
    completion_window.resizable(False, False)
    
    ttk.Label(completion_window, text="Encryption Completed!").pack(pady=10)
    
    button_frame = ttk.Frame(completion_window)
    button_frame.pack(pady=10)

    close_button = ttk.Button(button_frame, text="Close", command=window.quit)
    close_button.grid(row=0, column=0, padx=5)

    open_folder_button = ttk.Button(button_frame, text="Open Folder", command=lambda: open_output_folder(output_path))
    open_folder_button.grid(row=0, column=1, padx=5)

window = ThemedTk(theme="plastik")
window.title("PMXencrypt")
window.resizable(False, False)

# Create a style object
style = ttk.Style()

# Set the style for Entry widgets
style.map("EntryField.TEntry",
          fieldbackground=[("active", "#dddddd"), ("!active", "white")],
          background=[("active", "#dddddd"), ("!active", "white")],
          foreground=[("active", "black"), ("!active", "black")])

# Set the style for Button widgets
style.map("Button.TButton",
          background=[("active", "#4caf50"), ("!active", "SystemButtonFace")],
          relief=[("active", "raised"), ("!active", "flat")])

# Input file path
input_file_label = ttk.Label(window, text="Input File Path:")
input_file_label.grid(row=0, column=0, padx=10, pady=5)
input_file_entry = ttk.Entry(window, width=40, style="EntryField.TEntry")
input_file_entry.grid(row=0, column=1, padx=10, pady=5)
input_file_button = ttk.Button(window, text="Browse", command=select_input_file, style="Button.TButton")
input_file_button.grid(row=0, column=2, padx=10, pady=5)

# Output path
output_path_label = ttk.Label(window, text="Output Path:")
output_path_label.grid(row=1, column=0, padx=10, pady=5)
output_path_entry = ttk.Entry(window, width=40, style="EntryField.TEntry")
output_path_entry.grid(row=1, column=1, padx=10, pady=5)
output_path_button = ttk.Button(window, text="Browse", command=select_output_path, style="Button.TButton")
output_path_button.grid(row=1, column=2, padx=10, pady=5)

# Output file name
output_file_name_label = ttk.Label(window, text="Output File Name:")
output_file_name_label.grid(row=2, column=0, padx=10, pady=5)
output_file_name_entry = ttk.Entry(window, width=40, style="EntryField.TEntry")
output_file_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Start the obsfucation button
process_button = ttk.Button(window, text="GO!", command=start_processing, style="Button.TButton")
process_button.grid(row=3, column=1, pady=10)

# Start the GUI event loop
window.mainloop()
