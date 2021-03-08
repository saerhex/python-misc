import re
import os
import sys
from glob import glob
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from window import Ui_MainWindow


def setup():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"
    os.environ["PARSE_PATH"] = os.getcwd()


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.text = ""

        self.ui.pushButton.clicked.connect(self.click_read)

        self.ui.pushButton_2.clicked.connect(self.click_open)

    @pyqtSlot()
    def click_read(self):
        self.text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText("")
        self.parse()

    def parse(self):
        """
        Simple parser for local html-documents.

        You can change working directory by overwriting 
        environment variable "PARSE_PATH" if necessary.
        """
        words = self.text.split(',')
        template = '|'.join(words)
        cwd_path = os.environ["PARSE_PATH"]
        os.chdir(cwd_path)
        files = glob('source/*.html')
        occurs = []
        for file in files:
            with open(file, 'r') as f:
                occurs.append((file, re.findall(template, f.read())))
        max_file_name = max(occurs, key=lambda x: x[1])[0]
        self.max_file_path = "\\".join([cwd_path, max_file_name])

    @pyqtSlot()
    def click_open(self):
        os.system(self.max_file_path)


if __name__ == '__main__':
    setup()
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()

    sys.exit(app.exec())
