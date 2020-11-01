import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget


class ConvertWidget(QWidget):
    def __init__(self):
        super(ConvertWidget, self).__init__()
        self.play_button = QPushButton("play_button")
        self.stop_button = QPushButton("stop_button")
        self.play_button.clicked.connect(self.startTimer)
        self.stop_button.clicked.connect(self.stopTimer)
        self.minutes = 24
        self.seconds = 59

    def timer(self, flag=0):
        if flag == 0:
            for i in range(0, 1799, -1):
                self.minutes = i // 60
                self.seconds = i % 60

    def startTimer(self):
        print('Hello')

    def stopTimer(self):
        print('Goodbuy')


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        super().__init__()
        uic.loadUi('sunflower.ui', self)
        self.setWindowTitle('Sunflower')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
