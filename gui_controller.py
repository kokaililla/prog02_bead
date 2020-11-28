import sys
from labirintus import getMaze
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import Ui_MainWindow
from labWin import Ui_Dialog
from PySide2.QtWidgets import QMainWindow


class Controller:

    def __init__(self):
        self.mw = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mw)

        self.ui.b_Start.clicked.connect(self.clickStart)
        self.ui.b_Exit.clicked.connect(self.clickExit)

        self.ui.b_Result.clicked.connect(self.clickResult)

        self.mw.show()

    def clickExit(self):
        pass

    def clickStart(self):
        pass

    def clickResult(self):
        # self.child_win = labWin.Ui_Dialog(self)
        self.child_win.show()

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
