from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as f:
            f.write(key)

    return open(KEY_FILE, "rb").read()


cipher = Fernet(load_key())


def encrypt_file(data):
    return cipher.encrypt(data)


def decrypt_file(data):
    return cipher.decrypt(data)