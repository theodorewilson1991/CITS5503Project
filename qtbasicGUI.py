import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        calcbtn = QPushButton('Calculate', self)
        calbtn.clicked.connect(QCoreApplication.instance().quit)
        calcbtn.resize(calcbtn.sizeHint())
        calcbtn.move(250, 100)

        brsbtn1 = QPushButton('Browse', self)
        brsbtn1.clicked.connect(QCoreApplication.instance().quit)
        brsbtn1.resize(brsbtn.sizeHint())
        brsbtn1.move(350, 25)

        brsbtn2 = QPushButton('Browse', self)
        brsbtn2.clicked.connect(QCoreApplication.instance().quit)
        brsbtn2.resize(brsbtn.sizeHint())
        brsbtn2.move(350, 55)

        extbtn = QPushButton('Exit', self)
        extbtn.clicked.connect(QCoreApplication.instance().quit)
        extbtn.resize(extbtn.sizeHint())
        extbtn.move(350, 100)

        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('VTPS')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
