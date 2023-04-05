from itertools import cycle

def encrypt(plain_text, key):
    key_stream = cycle(key)
    cipher_text = ""

    for char in plain_text:
        if not char.isalpha():
            cipher_text += char
            continue
        char_ascii = ord(char.lower()) - 97
        key_ascii = ord(next(key_stream).lower()) - 97
        cipher_ascii = (char_ascii + key_ascii) % 26 + 97
        cipher_text += chr(cipher_ascii)

    return cipher_text

def decrypt(cipher_text, key):
    key_stream = cycle(key)
    plain_text = ""

    for char in cipher_text:
        if not char.isalpha():
            plain_text += char
            continue
        char_ascii = ord(char.lower()) - 97
        key_ascii = ord(next(key_stream).lower()) - 97
        plain_ascii = (char_ascii - key_ascii) % 26 + 97
        plain_text += chr(plain_ascii)

    return plain_text

print("Choose an operation:")
print("1. Encryption")
print("2. Decryption")
operation_choice = input("Enter your choice (1 or 2): ")

if operation_choice == "1":
    plain_text = input("Enter the text to be encrypted: ")
    key = input("Enter the encryption key: ")
    cipher_text = encrypt(plain_text, key)
    print(f"Encrypted text: {cipher_text}")
elif operation_choice == "2":
    cipher_text = input("Enter the text to be decrypted: ")
    key = input("Enter the decryption key: ")
    plain_text = decrypt(cipher_text, key)
    print(f"Decrypted text: {plain_text}")
else:
    print("Invalid choice. Please enter 1 or 2.")
