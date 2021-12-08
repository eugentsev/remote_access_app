

class Encryptor:
    def __init__(self):
        self.key = 1

    def encrypt(self, message):
        encrypt_message = ""
        for symb in message:
            encrypt_message += chr(ord(symb) + self.key)
        return encrypt_message
