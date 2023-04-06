import random
import time

def encrypt(message, key):
    # convert message to binary format
    message_bin = ''.join(format(ord(c), '08b') for c in message)
    print("Message in binary format:", message_bin)

    # generate a random number using system time and user input
    seed = str(key) + str(int(time.time()))
    random.seed(seed)
    random_num = random.getrandbits(len(message_bin))
    print("Random number used for encryption:", random_num)

    # perform XOR operation between the message and random number
    xor_result = int(message_bin, 2) ^ random_num
    print("Result of XOR operation:", xor_result)

    # perform modulo operation using the key
    encrypted_result = xor_result % key
    print("Encrypted message:", encrypted_result)

    return encrypted_result


def decrypt(encrypted_message, key, random_num):
    # convert the encrypted message to an integer
    encrypted_message = int(encrypted_message)

    # perform inverse modulo operation using the key
    inverse_result = encrypted_message ** -1 % key

    # perform XOR operation with the same random number used for encryption
    decrypted_result = inverse_result ^ random_num

    # convert binary format back to string format
    decrypted_message = ''.join(chr(int(decrypted_result[i:i+8], 2)) for i in range(0, len(bin(decrypted_result)[2:]), 8))

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
