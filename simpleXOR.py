import base64

def xor_cipher(text, key):
    # convert the text and key to binary strings
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_key = ''.join(format(ord(char), '08b') for char in key)
    print("Text in binary: ", binary_text)
    print("Key in binary: ", binary_key)
    
    # XOR the binary strings
    binary_result = ''
    for i in range(len(binary_text)):
        binary_result += str(int(binary_text[i]) ^ int(binary_key[i % len(binary_key)]))
    print("Result of XOR operation: ", binary_result)
    
    # convert the binary result to text
    result = ''
    for i in range(0, len(binary_result), 8):
        result += chr(int(binary_result[i:i+8], 2))
    
    return result

# main loop
while True:
    choice = input("Enter 1 for encryption, 2 for decryption, or 3 to exit: ")
    
    if choice == '1':
        text = input("Enter text to encrypt: ")
        key = input("Enter encryption key: ")
        
        # check if input is already Base64-encoded
        try:
            text = base64.b64decode(text).decode()
            print("Input is Base64-encoded.")
        except:
            print("Input is plaintext.")
        
        result = xor_cipher(text, key)
        encoded_result = base64.b64encode(result.encode()).decode()
        print("Encryption result: ", encoded_result)
    
    elif choice == '2':
        encoded_text = input("Enter text to decrypt: ")
        key = input("Enter decryption key: ")
        
        # check if input is already Base64-encoded
        try:
            text = base64.b64decode(encoded_text).decode()
            print("Input is Base64-encoded.")
        except:
            text = encoded_text
            print("Input is plaintext.")
        
        result = xor_cipher(text, key)
        print("Decryption result: ", result)
    
    elif choice == '3':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
