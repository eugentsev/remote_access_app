import socket

from authentificate import check_user


class SocketTcp:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_name = 'localhost'
        self.port = 6543
        self.info = []
        self.info_auth = None

    def main(self):
        self.socket_tcp_connection()
        self.socket_tcp_accept_messages()

    def list_info(self):
        self.info_auth = {
            'username': self.info[0],
            'password': self.info[1],
            'ip_address_mac': self.info[2],
        }
        return self.info_auth

    def socket_tcp_connection(self):
        print(self.server_name)
        server_address = (self.server_name, self.port)
        print('starting up on %s port %s' % server_address)
        self.sock.bind(server_address)
        self.sock.listen(1)

    def socket_tcp_accept_messages(self):
        while True:
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print('client connected:', client_address)
                while True:
                    data = connection.recv(255)
                    info = data.decode('utf-8')
                    self.info.append(info)
                    if len(self.info) == 3:
                        self.list_info()
                        message = check_user(self.info_auth)
                        connection.send(message.encode('utf-8'))
                        connection.close()
                        self.info = []
                    connection.send(' '.encode('utf-8'))
            except OSError:
                connection.close()
            finally:
                connection.close()

