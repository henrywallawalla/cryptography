def alphabet_wrap(startchar, shiftvalue):
    start_offset = ord(startchar) - ord("A")
    final_offset = (start_offset + shiftvalue) % 26
    return chr(final_offset + ord("A"))

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = []  
    if len(plaintext) == 0:
        return ""
    for char in plaintext:
        if(ord("A") <= ord(char) <= ord("Z")):
            encrypted.append(alphabet_wrap(char, offset))
        else:
            encrypted.append(char)
    return ("".join(encrypted)).strip()
            

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = []  
    if len(ciphertext) == 0:
        return ""
    for char in ciphertext:
        if(ord("A") <= ord(char) <= ord("Z")):
            decrypted.append(alphabet_wrap(char, -1 * offset))
        else:
            decrypted.append(char)
    return ("".join(decrypted)).strip()


# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted = []
    ##making the key
    fittedkey = ""
    for i in range((len(plaintext) // len(keyword)) + 1):
        fittedkey += keyword
    fittedkey = fittedkey[: len(plaintext)]

    for index in range(len(plaintext)):
            encrypted.append(alphabet_wrap(plaintext[index], ord(fittedkey[index]) - ord("A")))
    return ("".join(encrypted)).strip()

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypted = []
    fittedkey = ""
    for i in range((len(ciphertext) // len(keyword)) + 1):
        fittedkey += keyword
    fittedkey = fittedkey[: len(ciphertext)]

    for index in range(len(ciphertext)):
            decrypted.append(alphabet_wrap(ciphertext[index], -1 * ord(fittedkey[index]) - ord("A")))
    return ("".join(decrypted)).strip()

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    ##print(encrypt_caesar("111.A", 3))
    ##print(decrypt_caesar("111.A", 3))
    print(encrypt_vigenere("GEEKSFORGEEKS", "AYUSH"))
    print(decrypt_vigenere("GCYCZFMLYLEIM", "AYUSH"))

if __name__ == "__main__":
    main()