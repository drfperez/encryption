''' New encryption algorithm for educational purposes 
created by professor Francisco Pérez
The objective of the algorithm is to encrypt and 
decrypt a plain text message using a user-provided key 
and a random number generated using the system time 
and the key. 

The algorithm works by converting the plain text 
message to binary format and generating a random number 
using the user key and the current system time. 
The algorithm then performs an XOR operation between 
the binary message and the random number, and then 
performs a modulo operation using the user-provided 
key to generate the encrypted message.

To decrypt the message, the algorithm first 
performs an inverse modulo operation to get the 
original XOR result. It then performs an XOR operation 
between the XOR result and the same random number 
used for encryption, and then converts the binary format 
of the decrypted result back to string format.

The algorithm ensures that the random number 
generated for encryption is unique by using 
the user key and the current system time as 
the seed for the random number generator. 
This ensures that even if the same message 
is encrypted multiple times using the same key, the encrypted message will be different each time due to the use of a different random number generated using the current system time. The user must also provide the same random number used for encryption to decrypt the message, which ensures that only the person who knows the random number can decrypt the message.

'''

import random
import time

def encrypt(message, key):
    # convert message to binary format
    message_bin = ''.join(format(ord(c), '08b') for c in message)

    # generate a random number using system time and user input
    seed = str(key) + str(int(time.time()))
    random.seed(seed)
    random_num = random.getrandbits(len(message_bin))
    print("Random number used for encryption: ", random_num)

    # perform XOR operation between the message and random number
    xor_result = int(message_bin, 2) ^ random_num

    # perform modulo operation using the key
    encrypted_result = xor_result % key

    return encrypted_result


def decrypt(encrypted_message, key, random_num):
    # perform inverse modulo operation using the key
    inverse_result = encrypted_message ** -1 % key

    # perform XOR operation with the same random number used for encryption
    decrypted_result = inverse_result ^ random_num

    # convert binary format back to string format
    decrypted_message = ''.join(chr(int(decrypted_result[i:i+8], 2)) for i in range(0, len(decrypted_result), 8))

    return decrypted_message


def main():
    message = input("Enter the plain text message: ")
    key = int(input("Enter the key: "))
    choice = int(input("Enter 1 to encrypt or 2 to decrypt: "))

    if choice == 1:
        encrypted_message = encrypt(message, key)
        print("Encrypted message: ", encrypted_message)
    elif choice == 2:
        random_num = int(input("Enter the random number used for encryption: "))
        decrypted_message = decrypt(message, key, random_num)
        print("Decrypted message: ", decrypted_message)
    else:
        print("Invalid choice. Please enter 1 to encrypt or 2 to decrypt.")

if __name__ == '__main__':
    main()
