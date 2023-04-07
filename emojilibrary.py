import binascii
import emoji

def generate_emoji_dict():
    emoji_dict = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    
    # Generate emojis for each letter in the alphabet
    for letter in alphabet:
        emoji_key = f':regional_indicator_{letter}:'
        emoji_value = emoji.emojize(emoji_key)
        emoji_dict[letter] = emoji_value
    
    # Generate emojis for each number
    for num in numbers:
        emoji_key = f':{num}:'
        emoji_value = emoji.emojize(emoji_key)
        emoji_dict[num] = emoji_value
        
    return emoji_dict

def encrypt(plaintext, key, emoji_dict):
    encrypted_text = ''
    for char in plaintext:
        char_code = (ord(char) + key) % len(emoji_dict)
        encrypted_text += emoji_dict[list(emoji_dict.keys())[char_code]]
    return encrypted_text

def decrypt(encrypted_text, key, emoji_dict):
    text = ''
    for emoji_char in encrypted_text.split():
        char_code = list(emoji_dict.keys())[list(emoji_dict.values()).index(emoji_char)]
        char_code = (char_code - key) % len(emoji_dict)
        text += list(emoji_dict.keys())[char_code]
    return text

emoji_dict = generate_emoji_dict()

while True:
    print("\nMENU\n1. Encrypt\n2. Decrypt\n3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the encryption key: "))
        encrypted_text = encrypt(plaintext, key, emoji_dict)
        print("Encrypted text (with emojis): ", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the encrypted text: ")
        key = int(input("Enter the decryption key: "))
        decrypted_text = decrypt(encrypted_text, key, emoji_dict)
        print("Decrypted text: ", decrypted_text)
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
