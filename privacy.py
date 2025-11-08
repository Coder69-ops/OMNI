from cryptography.fernet import Fernet
import os

# Generate a key for encryption. In a real app, you'd save this securely.
if not os.path.exists("secret.key"): 
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file: key_file.write(key)

def encrypt_data(data):
    """
    Encrypts the given data.
    """
    with open("secret.key", "rb") as key_file: key = key_file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """
    Decrypts the given data.
    """
    with open("secret.key", "rb") as key_file: key = key_file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

def confirm_action(prompt):
    """
    Asks for user confirmation before executing a sensitive action.
    """
    response = input(f"{prompt} (y/n): ")
    return response.lower() == 'y'
