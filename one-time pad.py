import string

def encrypt(plaintext, key):
    ciphertext = ""
    for i, c in enumerate(plaintext):
        shift = string.ascii_lowercase.index(key[i])
        ciphertext += chr((ord(c) - 97 + shift) % 26 + 97)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for i, c in enumerate(ciphertext):
        shift = string.ascii_lowercase.index(key[i])
        plaintext += chr((ord(c) - 97 - shift) % 26 + 97)
    return plaintext

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Enter choice (1, 2, or 3): "))
        if choice == 1:
            plaintext = input("Enter plaintext: ")
            key = input("Enter one-time pad key: ")
            ciphertext = encrypt(plaintext, key)
            print("Plaintext: ", plaintext)
            print("Key: ", key)
            print("Ciphertext: ", ciphertext)
        elif choice == 2:
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter one-time pad key: ")
            plaintext = decrypt(ciphertext, key)
            print("Ciphertext: ", ciphertext)
            print("Key: ", key)
            print("Plaintext: ", plaintext)
        elif choice == 3:
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
