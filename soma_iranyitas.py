import sys
from labirintus import getMaze
from PyQt5 import QtGui
from PyQt5.QtCore import (
    Qt,
    QBasicTimer, QLineF
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsLineItem,
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,QMessageBox
    )



class Walls(QGraphicsRectItem):

    walls = []
    def __init__(self, parent=None):
        QGraphicsRectItem.__init__(self, parent)
        self.setRect(0, 0, 40, 40)
        Walls.walls.append((self.x(), self.y()))
        print(self.x(), self.y())


class FinishLine(QGraphicsLineItem):

    def __init__(self, parent=None):
        QGraphicsLineItem.__init__(self, parent)
        self.setLine(920, 600, 960, 600)


class Player(QGraphicsRectItem):

    def __init__(self, parent=None):
        QGraphicsRectItem.__init__(self, parent)
        self.setRect(0, 0, 40 , 40)
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.setBrush(Qt.red)


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:

        try:
            colliding_items = self.collidingItems()
            for item in colliding_items:
                if type(item) == type(FinishLine()):
                    msg = QMessageBox()
                    msg.setText("Nyertel")
                    msg.exec()
                    sys.exit()
            if event.key() == Qt.Key_Right:
                if self.x() <920:
                    move_to_x = self.x()+40
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Left:
                if self.x() >0:
                    move_to_x = self.x()-40
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Up:
                if self.y()>0:
                    move_to_x = self.x()
                    move_to_y = self.y() -40
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Down:
                if self.y() <600:
                    move_to_x = self.x()
                    move_to_y = self.y() +40
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)

        except Exception as e:
            print(e)

class Scene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        #a labirintus 2D-tömbben:
        t_maze2 = getMaze()


        # for i in range(0, len(t_maze2)):
        #     for j in range(0, len(t_maze2)):
        #         # print(t_maze2[i][j])
        #         x = 140
        #         y = 140
        #         if t_maze2[i][j] == "2" or t_maze2[i][j] == "3":
        #             print(t_maze2[i][j])
        #             wall = Walls()
        #             wall.setPos(x, y)
        #             Walls.walls.append((wall.x(), wall.y()))
        #             self.addItem(wall)
        #             x += 20
        #             y += 20




        wall1 = Walls()
        wall2 = Walls()
        wall3 = Walls()



        wall1.setPos(80, 80)
        wall2.setPos(120, 80)
        wall3.setPos(120, 120)


        Walls.walls.append((wall1.x(),wall1.y()))
        Walls.walls.append((wall2.x(), wall2.y()))
        Walls.walls.append((wall3.x(), wall3.y()))

        print(wall1.pos())

        self.addItem(wall1)
        self.addItem(wall2)
        self.addItem(wall3)

        self.finish = FinishLine()
        self.addItem(self.finish)
        self.player = Player()
        self.addItem(self.player)
        self.player.setFocus()

        print(self.player.pos())

        self.view = QGraphicsView(self)
        self.view.setFixedSize(960, 640)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSceneRect(0, 0, 960, 640)
        self.view.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scene()
    sys.exit(app.exec())