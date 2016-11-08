from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt, pyqtSlot, QTimer, QPointF
from PyQt5.QtGui import QBrush, QTransform, QWindow, QPainter

from grid import Grid

class AStarApplication(QWidget):

    pass

class Tile(QGraphicsItem):
    def __init__(self, node):
        self.node = node
        self.subtext = ''

    
    def set_subtext(self, text):
        self.subtext = text


    def _set_color(self, color):
        self._color = color


    def paint(self, painter, options, widget):
        painter.setBrush(color)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRect(self.node.x*10, self.node.y*10, 10, 10)

