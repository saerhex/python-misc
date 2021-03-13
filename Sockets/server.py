import socket


ADDRESS = ('localhost', 5005)
money_count = 50


def main():
    global money_count
    with TCPServer(10, ADDRESS).server as serv:
        while True:
            try:
                client, address = serv.accept()
            except socket.error:
                pass
            else:
                message = client.recv(4096).decode('utf-8')
                try:
                    m_mod = int(message)
                except ValueError:
                    m_mod = 0
                money_count += m_mod
                resp = f"Total balance: {str(money_count)}."

                print(resp)
                client.send(bytes(resp, encoding='UTF-8'))
                client.close()


class TCPServer:

    def __init__(self, query_len, address=None):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(address)
        self.server.listen(query_len)


if __name__ == '__main__':
    main()
