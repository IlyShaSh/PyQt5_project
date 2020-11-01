import sys
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Sunflower')
        uic.loadUi('sunflower.ui', self)

        self.play_button.clicked.connect(self.startTimer)
        self.stop_button.clicked.connect(self.stopTimer)

    def time(self, flag=0):
        print('Пошел')
        if flag == 0:
            for i in range(25, 0, -1):
                print(i)
                self.minutes.display(i // 60)
                self.seconds.display(i % 60)
                # QTimer.setInterval(1000)

    def startTimer(self):
        print('Hello')
        self.time()

    def stopTimer(self):
        print('Goodbye')
        self.time(flag=1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
