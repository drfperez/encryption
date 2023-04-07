
import base64
import hashlib

def generate_keys():
    """
    Generate a public and private key pair using SHA-256 hash function.
    Returns a tuple containing the public and private keys.
    """
    # Generate a random seed
    seed = b"my_secret_key"

    # Hash the seed using SHA-256
    hashed_seed = hashlib.sha256(seed).digest()

    # Split the hashed seed into two halves
    public_key = hashed_seed[:16]
    private_key = hashed_seed[16:]

    return public_key, private_key

def encrypt(message, public_key):
    """
    Encrypt a message using base64 encoding and the public key.
    Returns the encrypted message.
    """
    # Convert message to bytes
    message_bytes = message.encode()

    # XOR each byte of the message with the corresponding byte of the public key
    encrypted_bytes = bytes([message_bytes[i] ^ public_key[i % len(public_key)] for i in range(len(message_bytes))])

    # Encode the encrypted bytes using base64
    encrypted_message = base64.b64encode(encrypted_bytes).decode()

    return encrypted_message

def decrypt(encrypted_message, private_key):
    """
    Decrypt an encrypted message using base64 decoding and the private key.
    Returns the decrypted message.
    """
    # Decode the encrypted message using base64
    encrypted_bytes = base64.b64decode(encrypted_message.encode())

    # XOR each byte of the encrypted message with the corresponding byte of the private key
    decrypted_bytes = bytes([encrypted_bytes[i] ^ private_key[i % len(private_key)] for i in range(len(encrypted_bytes))])

    # Convert decrypted bytes to a string
    decrypted_message = decrypted_bytes.decode()

    return decrypted_message

# Main program loop
while True:
    # Print menu
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    # Get user input
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        # Generate public and private keys
        public_key, private_key = generate_keys()

        # Get message from user
        message = input("Enter message to encrypt: ")

        # Encrypt the message
        encrypted_message = encrypt(message, public_key)

        # Print intermediate steps and final result
        print("Public key: ", public_key)
        print("Encrypted message (base64): ", encrypted_message)

    elif choice == "2":
        # Get private key from user
        private_key = input("Enter private key: ")

        # Get encrypted message from user
        encrypted_message = input("Enter message to decrypt (base64): ")

        # Decrypt the message
        decrypted_message = decrypt(encrypted_message, private_key.encode())

        # Print intermediate steps and final result
        print("Private key: ", private_key.encode())
        print("Decrypted message: ", decrypted_message)

    elif choice == "3":
        # Exit program
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
