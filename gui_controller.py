import sys
from labirintus import getMaze
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import Ui_MainWindow
from labWin import Ui_Dialog
from PySide2.QtWidgets import QMainWindow, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox

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
        print("Na")
        msg = QMessageBox()
        msg.setWindowTitle("Kilépés megerősítése")
        msg.setText("Biztosan ki akar lépni?")
        msg.setInformativeText("Kilépés esetén a mentés nem végezhető el.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)

        msg.buttonClicked.connect(self.popup_button)
        msg.exec_()

    def popup_button(self, i):
        print(i.text())
        if i.text() == "OK":
            QtWidgets.QApplication.instance().quit()

    def clickStart(self):
        pass

    def clickResult(self):
        pass
        # self.child_win = labWin.Ui_Dialog(self)
        # self.child_win.show()

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
