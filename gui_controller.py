import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow

class Controller:

    def __init__(self):
        self.mw = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mw)

        self.ui.b_Start.clicked.connect(self.clickStart)
        self.ui.b_Exit.clicked.connect(self.clickExit)

        self.mw.show()



    def clickExit(self):
        print("Kiléptem")

    def clickStart(self):
        pass

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
