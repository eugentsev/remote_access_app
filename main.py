from tcp_server import SocketTcp

if __name__ == '__main__':
    app = SocketTcp()
    try:
        app.main()
    except KeyboardInterrupt:
        print('application_interrupt')

