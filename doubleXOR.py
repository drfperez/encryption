
import base64

def xor_cipher(text, keys):
    # convert the text and keys to binary strings
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    print("Text in binary: ", binary_text)
    
    # XOR the binary string with each key in sequence
    binary_result = binary_text
    for key in keys:
        binary_key = ''.join(format(ord(char), '08b') for char in key)
        print("Key in binary: ", binary_key)
        binary_round = ''
        for i in range(len(binary_text)):
            binary_round += str(int(binary_result[i]) ^ int(binary_key[i % len(binary_key)]))
        binary_result = binary_round
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
        key1 = input("Enter encryption key 1: ")
        key2 = input("Enter encryption key 2: ")
        
        # check if input is already Base64-encoded
        try:
            text = base64.b64decode(text).decode()
            print("Input is Base64-encoded.")
        except:
            print("Input is plaintext.")
        
        result = xor_cipher(text, [key1, key2])
        encoded_result = base64.b64encode(result.encode()).decode()
        print("Encryption result: ", encoded_result)
    
    elif choice == '2':
        encoded_text = input("Enter text to decrypt: ")
        key1 = input("Enter decryption key 1: ")
        key2 = input("Enter decryption key 2: ")
        
        # check if input is already Base64-encoded
        try:
            text = base64.b64decode(encoded_text).decode()
            print("Input is Base64-encoded.")
        except:
            text = encoded_text
            print("Input is plaintext.")
        
        result = xor_cipher(text, [key2, key1])
        print("Decryption result: ", result)
    
    elif choice == '3':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
