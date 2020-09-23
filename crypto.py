def alphabet_wrap(startchar, shiftvalue):
    if ord(startchar) + shiftvalue > ord("Z"):
        return chr(ord("A") + (ord("Z") - (ord(startchar) + shiftvalue)))
    return chr(ord(startchar) + shiftvalue)

def backwards_alphabet_wrap(startchar, shiftvalue):
    if ord(startchar) - shiftvalue < ord("A"):
        return chr(1 + ord("Z") - (shiftvalue - (ord(startchar) - ord("A"))))
    return chr(ord(startchar) - shiftvalue)

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
    return (" ".join(encrypted)).strip()
            

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = []  
    if len(ciphertext) == 0:
        return ""
    for char in ciphertext:
        if(ord("A") <= ord(char) <= ord("Z")):
            decrypted.append(backwards_alphabet_wrap(char, offset))
        else:
            decrypted.append(char)
    return (" ".join(decrypted)).strip()

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

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
    ##print(alphabet_wrap("A", 1))
    print(encrypt_caesar("EGAN LAI!!", 3))
    ##print(backwards_alphabet_wrap("A", 1))
    print(decrypt_caesar("HJDQ ODL!!", 3))

if __name__ == "__main__":
    main()