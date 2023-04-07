import base64
import hashlib
import secrets

def generate_keys():
    """
    Generate a public and private key pair using SHA-256 hash function.
    Returns a tuple containing the public and private keys.
    """
    # Generate a random seed
    seed = secrets.token_bytes(16)

    # Hash the seed using SHA-256
    hashed_seed = hashlib.sha256(seed).digest()

    # Split the hashed seed into two halves
    public_key = hashed_seed[:16]
    private_key = hashed_seed[16:]

    # Generate personal key using SHA-256 and the private key
    personal_key = hashlib.sha256(private_key).digest()

    print("Generated keys:")
    print("Public key: ", public_key)
    print("Private key: ", private_key)
    print("Personal key: ", personal_key)

    return public_key, private_key, personal_key

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

    print("Encryption:")
    print("Message: ", message)
    print("Public key: ", public_key)
    print("Message (bytes): ", message_bytes)
    print("XORed bytes: ", encrypted_bytes)
    print("Encrypted message (base64): ", encrypted_message)

    return encrypted_message

def decrypt(encrypted_message, personal_key):
    """
    Decrypt an encrypted message using base64 decoding and the personal key.
    Returns the decrypted message.
    """
    # Decode the encrypted message using base64
    encrypted_bytes = base64.b64decode(encrypted_message.encode())

    # XOR each byte of the encrypted message with the corresponding byte of the personal key
    decrypted_bytes = bytes([encrypted_bytes[i] ^ personal_key[i % len(personal_key)] for i in range(len(encrypted_bytes))])

    # Convert decrypted bytes to a string
    decrypted_message = decrypted_bytes.decode()

    print("Decryption:")
    print("Encrypted message (base64): ", encrypted_message)
    print("Personal key: ", personal_key)
    print("XORed bytes: ", decrypted_bytes)
    print("Decrypted message: ", decrypted_message)

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
        # Generate public, private and personal keys
        public_key, private_key, personal_key = generate_keys()

        # Get message from user
        message = input("Enter message to encrypt: ")

        # Encrypt the message
        encrypted_message = encrypt(message, public_key)

    elif choice == "2":
        # Get personal key from user
        personal_key = input("Enter personal key: ")

        # Get encrypted message from user
        encrypted_message = input("Enter message to decrypt (base64): ")

        # Decrypt the message
        decrypted_message = decrypt(encrypted_message, personal_key.encode())

    elif choice == "3":
        # Exit program
        break

    else:
        print("Invalid choice. Please choose 1,2 or 3")
