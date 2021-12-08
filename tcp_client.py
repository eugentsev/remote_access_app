import socket
import hashlib
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
from ipconfig import IPv4
from mac_address import MAC


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 6543)
        self.key = None
        self.public = None
        self.private = None

    # def rsa_key(self, key_size):
        # public key and private key
        # random_generator = Random.new().read
        # self.key = RSA.generate(key_size, random_generator)
        # self.public = self.key.publickey()
        # self.private = self.key.exportKey()
        # # hashing the public key
        # hash_object = hashlib.sha1(self.public)
        # hex_digest = hash_object.hexdigest()

    def connection(self):
        print('connecting to %s port %s' % self.server_address)
        self.sock.connect(self.server_address)

    def recv(self):
        message = self.sock.recv(1024)
        encryptor = PKCS1_OAEP.new(self.public)
        dec_message = encryptor.decrypt(message)

    def send_message(self, username, password):
        while True:
            # encryptor = PKCS1_OAEP.new(self.public)
            # enc_message = encryptor.encrypt(message.encode('utf-8'))
            try:
                addresses = str(IPv4 + MAC)
                info = (username, password, addresses)
                for item in info:
                    self.sock.send(item.encode('utf-8'))
                    data = self.sock.recv(1024)
                    message = data.decode('utf-8')
                    print(message)
                    if message != ' ':
                        return message
                self.sock.close()
            finally:
                self.sock.close()


if __name__ == '__main__':
    app = Client()
    app.connection()
    # app.rsa_key(1024)
    app.send_message('eugen8934', 'zheka8934')