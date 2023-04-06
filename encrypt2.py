from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, padding
import tkinter as tk
from tkinter import ttk

# Create a tkinter window
window = tk.Tk()
window.title("Encryption/Decryption")

# Create a label for the user to enter the text
text_label = tk.Label(window, text="Enter text:")
text_label.pack()

# Create a text box for the user to enter the text
text_entry = tk.Entry(window, width=50)
text_entry.pack()

# Create a label for the user to enter the key
key_label = tk.Label(window, text="Enter key:")
key_label.pack()

# Create a text box for the user to enter the key
key_entry = tk.Entry(window, width=50)
key_entry.pack()

# Create a dropdown menu for the user to select the algorithm
algorithm_label = tk.Label(window, text="Select algorithm:")
algorithm_label.pack()

algorithm_var = tk.StringVar(window)
algorithm_dropdown = ttk.Combobox(window, textvariable=algorithm_var,
                                  values=["Fernet", "AES", "TripleDES", "Blowfish", "ChaCha20"])
algorithm_dropdown.pack()

# Create a label to display the output
output_label = tk.Label(window)
output_label.pack()

# Function to encrypt the text using Fernet
def fernet_encrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()

    # Generate a key using the Fernet algorithm
    f = Fernet(key)

    # Encrypt the text using the key
    encrypted_text = f.encrypt(text)

    # Display the encrypted text to the user
    output_label.config(text=f"Encrypted text: {encrypted_text}")

# Function to decrypt the text using Fernet
def fernet_decrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()

    # Generate a key using the Fernet algorithm
    f = Fernet(key)

    # Decrypt the text using the key
    decrypted_text = f.decrypt(text)

    # Display the decrypted text to the user
    output_label.config(text=f"Decrypted text: {decrypted_text.decode()}")

# Function to encrypt the text using AES
def aes_encrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()

    # Generate a key and IV for AES encryption
    key_hash = hashes.Hash(hashes.SHA256())
    key_hash.update(key)
    key = key_hash.finalize()
    iv_hash = hashes.Hash(hashes.SHA256())
    iv_hash.update(text)
    iv = iv_hash.finalize()[:16]

    # Apply PKCS#7 padding to the plaintext
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_text = padder.update(text) + padder.finalize()
    # Encrypt the text using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()

    # Display the encrypted text to the user
    output_label.config(text=f"Encrypted text: {encrypted_text}")
# Function to decrypt the text using AES
def aes_decrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()
    # Generate a key and IV for AES encryption
    key_hash = hashes.Hash(hashes.SHA256())
    key_hash.update(key)
    key = key_hash.finalize()
    iv_hash = hashes.Hash(hashes.SHA256())
    iv_hash.update(text)
    iv = iv_hash.finalize()[:16]

    # Decrypt the text using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(text) + decryptor.finalize()

    # Remove PKCS#7 padding from the decrypted text
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()

    # Display the decrypted text to the user
    output_label.config(text=f"Decrypted text: {unpadded_text.decode()}")
    # Function to encrypt the text using TripleDES
def triple_des_encrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()
    # Generate a key and IV for TripleDES encryption
    key_hash = hashes.Hash(hashes.SHA256())
    key_hash.update(key)
    key = key_hash.finalize()[:24]
    iv_hash = hashes.Hash(hashes.SHA256())
    iv_hash.update(text)
    iv = iv_hash.finalize()[:8]

    # Apply PKCS#7 padding to the plaintext
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_text = padder.update(text) + padder.finalize()

    # Encrypt the text using the key and IV
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()

    # Display the encrypted text to the user
    output_label.config(text=f"Encrypted text: {encrypted_text}")

    #Function to decrypt the text using TripleDES
def triple_des_decrypt():
    # Get the text and key from the user input
    text = text_entry.get().encode()
    key = key_entry.get().encode()
# Generate a key and IV for TripleDES encryption
key_hash = hashes.Hash(hashes.SHA256())
key_hash.update(key)
key = key_hash.finalize()[:24]
iv_hash = hashes.Hash(hashes.SHA256())
iv_hash.update(text)
iv = iv_hash.finalize()[:8]

# Decrypt the text using the key and IV
cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
decrypted_text = decryptor.update(text) + decryptor.finalize()

# Remove PKCS#7 padding from the decrypted text
unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()

# Display the decrypted text to the user
output_label.config(text=f"Decrypted text: {unpadded_text.decode()}")
