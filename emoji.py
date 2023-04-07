import random

emojis = {
    'a': '😀',
    'b': '😂',
    'c': '😊',
    'd': '😍',
    'e': '🤔',
    'f': '😜',
    'g': '😎',
    'h': '😇',
    'i': '😉',
    'j': '🤯',
    'k': '😘',
    'l': '🥰',
    'm': '😋',
    'n': '🤢',
    'o': '😴',
    'p': '😷',
    'q': '👻',
    'r': '💩',
    's': '🤫',
    't': '😭',
    'u': '🤗',
    'v': '🤩',
    'w': '😱',
    'x': '🤔',
    'y': '🥺',
    'z': '🙃',
    ' ': '👽',
    '1': '🐶',
    '2': '🐱',
    '3': '🐻',
    '4': '🐼',
    '5': '🐨',
    '6': '🐯',
    '7': '🦁',
    '8': '🐷',
    '9': '🐸',
    '0': '🐢'
}

def encrypt(message, key):
    result = ''
    for char in message.lower():
        if char in emojis:
            result += emojis[char]
        else:
            result += char
    return result

def decrypt(message, key):
    result = ''
    for emoji in message.split():
        for char, emoji_char in emojis.items():
            if emoji == emoji_char:
                result += char
                break
    return result

while True:
    choice = input("Enter 1 to encrypt, 2 to decrypt, or 3 to exit: ")
    if choice == '1':
        message = input("Enter the message to encrypt: ")
        key = input("Enter the encryption key: ")
        encrypted_message = encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        key = input("Enter the decryption key: ")
        decrypted_message = decrypt(message, key)
        print("Decrypted message:", decrypted_message)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
