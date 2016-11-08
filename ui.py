from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt, pyqtSlot, QTimer, QPointF, QRectF
from PyQt5.QtGui import QBrush, QTransform, QWindow, QPainter

from grid import Grid

class AStarApplication(QWidget):
    def __init__(self):
        super(AStarApplication, self).__init__()

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.canvas = QGraphicsView()
        self.canvas.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.grid = Grid(24,16)
        self.tiles = []
        for x in range(self.grid.w):
            for y in range(self.grid.h):
                tile = Tile(self.grid.get_node(x,y))
                self.tiles.append(tile)

        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        
        for t in self.tiles:
            self.scene.addItem(t)
        
        self.canvas.setScene(self.scene)
        self.layout.addWidget(self.canvas)


class Tile(QGraphicsItem):
    size = 48
    
    def __init__(self, node):
        super(Tile, self).__init__()

        self.node = node
        self.subtext = ''

        self._color = Qt.white


    def set_subtext(self, text):
        self.subtext = text


    def _set_color(self, color):
        self._color = color


    def paint(self, painter, options, widget):
        painter.setBrush(self._color)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRect(self.node.x*self.size, self.node.y*self.size, self.size, self.size)


    def boundingRect(self):
        return QRectF(self.node.x*self.size, self.node.y*self.size, self.size, self.size)
