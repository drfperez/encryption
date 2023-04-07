import base64

def encrypt(plaintext, key):
    if len(key) < len(plaintext):
        raise ValueError("Error: Key must be at least as long as the plaintext.")
    
    # Convert the plaintext and key to byte strings
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Perform XOR between the plaintext and key
    ciphertext_bytes = bytes([plaintext_bytes[i] ^ key_bytes[i] for i in range(len(plaintext_bytes))])
    
    # Encode the resulting byte string as base64 for printing purposes
    ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')
    
    # Print intermediate steps and calculations
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext bytes: {list(plaintext_bytes)}")
    print(f"Key: {key}")
    print(f"Key bytes: {list(key_bytes)}")
    print(f"Plaintext XOR Key: {list(ciphertext_bytes)}")
    print(f"Ciphertext: {ciphertext}")
    
    return ciphertext

def decrypt(ciphertext, key):
    if len(key) < len(ciphertext):
        raise ValueError("Error: Key must be at least as long as the ciphertext.")
    
    # Convert the ciphertext and key to byte strings
    ciphertext_bytes = base64.b64decode(ciphertext.encode('utf-8'))
    key_bytes = key.encode('utf-8')
    
    # Perform XOR between the ciphertext and key
    plaintext_bytes = bytes([ciphertext_bytes[i] ^ key_bytes[i] for i in range(len(ciphertext_bytes))])
    
    # Decode the resulting byte string as UTF-8 for printing purposes
    plaintext = plaintext_bytes.decode('utf-8')
    
    # Print intermediate steps and calculations
    print(f"Ciphertext: {ciphertext}")
    print(f"Ciphertext bytes: {list(ciphertext_bytes)}")
    print(f"Key: {key}")
    print(f"Key bytes: {list(key_bytes)}")
    print(f"Ciphertext XOR Key: {list(plaintext_bytes)}")
    print(f"Plaintext: {plaintext}")
    
    return plaintext

def main():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter choice (1, 2, or 3): ")
        
        if choice == "1":
            plaintext = input("Enter plaintext: ")
            key = input("Enter one-time pad key: ")
            
            try:
                ciphertext = encrypt(plaintext, key)
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        elif choice == "2":
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter one-time pad key: ")
            
            try:
                plaintext = decrypt(ciphertext, key)
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        elif choice == "3":
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
