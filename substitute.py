import string
import random

def generate_key(user_key):
    """Generate a key from the user-provided key."""
    user_key = user_key.lower()
    key = list(dict.fromkeys(user_key)) # Remove duplicate characters
    for letter in string.ascii_lowercase:
        if letter not in key:
            key.append(letter)
    return ''.join(key)

def encrypt(plaintext, key):
    """Encrypt the plaintext using the provided key."""
    print("Generating key from user-provided key...")
    key = generate_key(key)
    print("Key: ", key)
    ciphertext = []
    for letter in plaintext:
        if letter.isalpha():
            index = string.ascii_lowercase.index(letter.lower())
            if letter.isupper():
                ciphertext.append(key[index].upper())
            else:
                ciphertext.append(key[index])
        else:
            ciphertext.append(letter)
    ciphertext = ''.join(ciphertext)
    print("Plaintext: ", plaintext)
    print("Ciphertext: ", ciphertext)
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the provided key."""
    print("Generating key from user-provided key...")
    key = generate_key(key)
    print("Key: ", key)
    plaintext = []
    for letter in ciphertext:
        if letter.isalpha():
            index = key.index(letter.lower())
            if letter.isupper():
                plaintext.append(string.ascii_uppercase[index])
            else:
                plaintext.append(string.ascii_lowercase[index])
        else:
            plaintext.append(letter)
    plaintext = ''.join(plaintext)
    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", plaintext)
    return plaintext

while True:
    choice = input("Enter 1 to encrypt or 2 to decrypt: ")
    if choice == '1':
        plaintext = input("Enter plaintext to encrypt: ")
        key = input("Enter key: ")
        ciphertext = encrypt(plaintext, key)
        print("Final ciphertext: ", ciphertext)
    elif choice == '2':
        ciphertext = input("Enter ciphertext to decrypt: ")
        key = input("Enter key: ")
        plaintext = decrypt(ciphertext, key)
        print("Final plaintext: ", plaintext)
    else:
        print("Invalid choice. Please try again.")
