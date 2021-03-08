import os
import sys
import socket
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import pyqtSlot
from window import Ui_MainWindow

DEST_PORT = input()
SRC_PORT = input()

DEST_ADDRESS = ('localhost', int(DEST_PORT))
SRC_ADDRESS = ('localhost', int(SRC_PORT))


def setup():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.click_send_msg)

    @pyqtSlot()
    def click_send_msg(self):
        text = self.ui.lineEdit.text()
        if not text:
            QMessageBox.critical(self, "Error", "Enter text under the button!", QMessageBox.Ok)
            return
        else:
            with TCPClient(DEST_ADDRESS).server as client:
                client.send(bytes(text, encoding='UTF-8'))
                text = client.recv(1024).decode('utf-8')
                self.ui.lineEdit_2.setText(text)


class TCPClient:

    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(address)


if __name__ == '__main__':
    setup()
    app = QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())
