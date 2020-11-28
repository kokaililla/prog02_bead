<<<<<<< HEAD
import sys
from labirintus import getMaze
from PyQt5 import QtGui
from PyQt5.QtCore import ( Qt, QBasicTimer, QLineF)
from PyQt5.QtGui import (QBrush, QPixmap)
from PyQt5.QtWidgets import (QGraphicsLineItem, QApplication, QGraphicsItem, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView,QMessageBox)


class Walls(QGraphicsPixmapItem):
    walls = []
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_fal.png'))

class Finish(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_cel.png'))

class Path(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_ut.png'))

class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_babu.png'))
        self.setFlag(QGraphicsItem.ItemIsFocusable)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        try:
            colliding_items = self.collidingItems()
            for item in colliding_items:
                if type(item) == type(Finish()):
                    self.setPixmap(QtGui.QPixmap('lab_nyert.png'))
                    msg = QMessageBox()
                    msg.setText("Nyertel")
                    msg.exec()
                    sys.exit()
            if event.key() == Qt.Key_Right:
                if self.x() <608:
                    move_to_x = self.x()+32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Left:
                if self.x() >0:
                    move_to_x = self.x()-32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Up:
                if self.y()>0:
                    move_to_x = self.x()
                    move_to_y = self.y() -32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Down:
                if self.y() <608:
                    move_to_x = self.x()
                    move_to_y = self.y() +32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)

        except Exception as e:
            print(e)

class Scene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        t_maze2 = getMaze()
        for i in range(len(t_maze2)):
            for j in range(len(t_maze2)):

                if t_maze2[i][j] == '1':
                    path = Path()
                    self.addItem(path)
                    path.setPos(i*32, j*32)
                if t_maze2[i][j]=='0':
                    wall=Walls()
                    self.addItem(wall)
                    wall.setPos(i*32, j*32)
                    Walls.walls.append((wall.x(), wall.y()))
                if t_maze2[i][j] == '2':
                    finish = Finish()
                    self.addItem(finish)
                    finish.setPos(i*32, j*32)
                if t_maze2[i][j] =='3':
                    path = Path()
                    self.addItem(path)
                    path.setPos(i*32, j*32)
                    x = i*32
                    y= j*32
        player = Player()
        self.addItem(player)
        player.setPos(x, y)
        player.setFocus()

        self.view = QGraphicsView(self)
        self.view.setFixedSize(640, 640)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSceneRect(0, 0, 640, 640)
        self.view.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scene()
    sys.exit(app.exec())

=======
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



class Walls(QGraphicsPixmapItem):
    walls = []
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_fal.png'))




class Finish(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_cel.png'))

class Path(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_ut.png'))



class Player(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QtGui.QPixmap('lab_babu.png'))
        self.setFlag(QGraphicsItem.ItemIsFocusable)




    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        try:
            colliding_items = self.collidingItems()
            for item in colliding_items:
                if type(item) == type(Finish()):
                    msg = QMessageBox()
                    msg.setText("Nyertel")
                    msg.exec()
                    sys.exit()
            if event.key() == Qt.Key_Right:
                if self.x() <352:
                    move_to_x = self.x()+32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Left:
                if self.x() >0:
                    move_to_x = self.x()-32
                    move_to_y = self.y()
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Up:
                if self.y()>0:
                    move_to_x = self.x()
                    move_to_y = self.y() -32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)
            if event.key() == Qt.Key_Down:
                if self.y() <352:
                    move_to_x = self.x()
                    move_to_y = self.y() +32
                    if (move_to_x, move_to_y) not in Walls.walls:
                        self.setPos(move_to_x, move_to_y)

        except Exception as e:
            print(e)








class Scene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)




        t_maze2 = getMaze()
        for i in range(len(t_maze2)):
            for j in range(len(t_maze2)):

                if t_maze2[i][j] == '1':
                    path = Path()
                    self.addItem(path)
                    path.setPos(i*32, j*32)
                if t_maze2[i][j]=='0':
                    wall=Walls()
                    self.addItem(wall)
                    wall.setPos(i*32, j*32)
                    Walls.walls.append((wall.x(), wall.y()))
                if t_maze2[i][j] == '2':
                    finish = Finish()
                    self.addItem(finish)
                    finish.setPos(i*32, j*32)
                if t_maze2[i][j] =='3':
                    path = Path()
                    self.addItem(path)
                    path.setPos(i*32, j*32)
                    x = i*32
                    y= j*32
        player = Player()
        self.addItem(player)
        player.setPos(x, y)
        player.setFocus()




        self.view = QGraphicsView(self)
        self.view.setFixedSize(384, 384)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSceneRect(0, 0, 384, 384)
        self.view.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scene()
    sys.exit(app.exec())

>>>>>>> 35aa2ba269e6d5f829aa9039fb53197e9be0d822
    t1 = getMaze()