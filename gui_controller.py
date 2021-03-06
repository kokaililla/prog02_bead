import sys

from labirintus import getMaze
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import Ui_MainWindow
from labWin import Ui_Dialog
from PySide2.QtWidgets import QMainWindow, QDialogButtonBox, QVBoxLayout, QDialog, QMessageBox
from Player import Player, MissingDataException

class Controller:

    def __init__(self):
        self.mw = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mw)

        self.ui.b_Start.clicked.connect(self.clickStart)
        self.ui.b_Exit.clicked.connect(self.clickExit)
        self.ui.b_Result.clicked.connect(self.clickResult)

        self.list = []

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

        name = "PLayer"
        try:
            if name == "":
                raise Exception('név')
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Hiba")
            msg.setText("Hiányzó " + str(e) + ".")
            msg.exec()

        self.curr_time = QtCore.QTime(00, 00, 00)
        self.timer0 = QtCore.QTimer()
        self.time = QtCore.QTime(00, 00, 00)
        self.timer0.setInterval(1000)
        self.timer0.timeout.connect(self.calc)
        self.timer0.start()
        self.ui.lcdNumber.display(str(self.calc()))

    def save2File(self, name, time):
        try:
            if name == "":
                raise MissingDataException("név")
            if time == "":
                raise MissingDataException("időtartam")

            fout = open("database.txt", "w")
            for w in self.list:
                w.save2File(fout)
            fout.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText('Hiba történt:\n' + e.__str__())
            msg.exec()

    def loadData(self):
        fin = open("database.txr", "r")
        for r in fin:
            ls = r.split(";")
            nw = Player(ls[0], ls[1], ls[2])
            self.list.append(nw)
        fin.close()


    def calc(self):
        global time
        self.time = self.time.addSecs(1)
        self.ui.lcdNumber.display(self.time.toString("hh:mm:ss"))


    def clickResult(self):
        name = QtWidgets.QApplication.ui.in_Name.text()
        print(name)

    #main
    # t_maze = getMaze()
    # print(t_maze[0][0])

#MAIN
app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec())
