import sys
from labirintus import getMaze
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

        t_maze = getMaze()

        self.ui.textEdit.setText(t_maze[0][0])
        self.ui.textEdit.setEnabled(False)

        self.mw.show()


    def clickExit(self):
        pass

    def clickStart(self):
        pass

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
