def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            plaintext += chr((ord(c) - shift - 97) % 26 + 97)
        else:
            plaintext += c
    return plaintext

def generate_keys(ciphertext):
    for i in range(1, 26):
        print("Key {}: {}".format(i, decrypt_caesar(ciphertext, i)))

ciphertext = input("Enter the ciphertext: ")
generate_keys(ciphertext)
