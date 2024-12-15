from cryptography.fernet import Fernet

class CryptographicProtocols:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_message(self, message):
        """Encrypt a message using symmetric encryption."""
        encrypted_message = self.cipher.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        """Decrypt a message using symmetric encryption."""
        decrypted_message = self.cipher.decrypt(encrypted_message).decode()
        return decrypted_message

if __name__ == "__main__":
    crypto = CryptographicProtocols()
    message = "Hello, secure world!"
    encrypted = crypto.encrypt_message(message)
    print("Encrypted Message:", encrypted)
    decrypted = crypto.decrypt_message(encrypted)
    print("Decrypted Message:", decrypted)
