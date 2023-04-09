import string

# Define the alphabet
alphabet = string.ascii_lowercase

def count_letters(text):
    """Count the frequency of each letter in the text"""
    freq = {}
    for c in text:
        if c.lower() in alphabet:
            freq[c.lower()] = freq.get(c.lower(), 0) + 1
    return freq

def propose_keys(ciphertext, freq):
    """Propose a set of possible keys based on letter frequencies"""
    keys = []
    for i in range(len(alphabet)):
        # Shift the alphabet by i positions to the right
        shift = alphabet[i:] + alphabet[:i]
        key = {}
        for j in range(len(alphabet)):
            # Map each letter in the ciphertext to a letter in the shifted alphabet
            key[shift[j]] = alphabet[j]
        # Apply the key to the ciphertext to obtain the plaintext
        plaintext = "".join([key.get(c.lower(), c) for c in ciphertext])
        # Count the frequency of each letter in the plaintext
        freq_plaintext = count_letters(plaintext)
        # Compute the difference in frequency between the plaintext and the expected frequency
        diff = sum([abs(freq.get(c, 0) - freq_plaintext.get(c, 0)) for c in alphabet])
        # If the difference is small enough, add the key to the list of possible keys
        if diff < 10:
            keys.append(key)
        
        print("i = ", i)
        print("shift = ", shift)
        print("key = ", key)
        print("plaintext = ", plaintext)
        print("freq_plaintext = ", freq_plaintext)
        print("diff = ", diff)
        print("------------------------")

    return keys

# Prompt the user to enter a ciphertext
ciphertext = input("Enter the ciphertext: ")

# Compute the frequency of each letter in the ciphertext
freq = count_letters(ciphertext)

# Propose a list of possible keys based on letter frequencies
keys = propose_keys(ciphertext, freq)

# Print the proposed keys, or a message indicating no keys were found
if not keys:
    print("No possible keys found.")
else:
    print("Possible keys:")
    for key in keys:
        print(key)
