import math
import random

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    """Generate a prime number in the given range."""
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    """Calculate modular multiplicative inverse of e mod phi."""
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod_inverse does not exist")

def generate_keypair():
    """Generate RSA public and private keys."""
    # Generate two prime numbers
    p = generate_prime(100, 1000)
    q = generate_prime(100, 1000)
    while p == q:
        q = generate_prime(100, 1000)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e: coprime to phi
    e = random.randint(3, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi - 1)
    
    # Calculate d: modular inverse of e
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypt a message using the public key."""
    e, n = public_key
    # Convert each character to a number and encrypt
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt a message using the private key."""
    d, n = private_key
    # Decrypt each number back to a character
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# Example usage
if __name__ == '__main__':
    print("Generating RSA key pair...")
    public_key, private_key = generate_keypair()
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")
    
    message = "Hello, RSA!"
    print(f"Original message: {message}")
    
    encrypted_msg = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_msg}")
    
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")
