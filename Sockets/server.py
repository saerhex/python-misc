import socket
import sys
from server_side import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

ADDRESS = ('localhost', 5005)


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.money_count = 50
        self.show()

        self.main()

    def main(self):
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
                    self.money_count += m_mod
                    resp = f"Total balance: {str(self.money_count)}."

                    self.ui.label.setText(resp)
                    client.send(bytes(resp, encoding='UTF-8'))
                    client.close()


class TCPServer:

    def __init__(self, query_len, address=None):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(address)
        self.server.listen(query_len)


if __name__ == '__main__':
    app = QApplication([])
    application = Window()
    sys.exit(app.exec())
