from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtCore import Qt, pyqtSlot, QTimer, QPointF, QRectF
from PyQt5.QtGui import QBrush, QTransform, QWindow, QPainter

from grid import Grid

# The window that's launched with the application
class AStarApplication(QWidget):
    def __init__(self):
        super(AStarApplication, self).__init__()
        self.close = self.cleanup

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.canvas = QGraphicsView()
        self.canvas.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.grid = Grid(24,20)
        self.tiles = []
        for x in range(self.grid.w):
            for y in range(self.grid.h):
                tile = Tile(self.grid.get_node(x,y), self)
                self.tiles.append(tile)

        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QBrush(Qt.lightGray, Qt.SolidPattern))
        
        for t in self.tiles:
            self.scene.addItem(t)
        
        self.canvas.setScene(self.scene)
        self.layout.addWidget(self.canvas)

        self.refresh_timer = QTimer()
        self.refresh_timer.setInterval(1000/60)
        self.refresh_timer.timeout.connect(self.refresh)
        self.refresh_timer.start()


    # Avoid the segfault caused by some obscure GC stuff.
    @pyqtSlot()
    def cleanup(self, obj):
        pass


    @pyqtSlot()
    def refresh(self):
        self.scene.invalidate()


    # Called when a tile changes type, so old 
    def update_tiles(self, caller):
        if caller.type == 'clear' or caller.type == 'wall':
            return
        for t in self.tiles:
            if t != caller and t.type == caller.type:
                t.set_type('clear')


# A QGraphicsItem that wraps a Node and is drawn as a tile
class Tile(QGraphicsItem):
    size = 48
    _colors = {'clear' : Qt.white, 'wall' : Qt.darkGray, 'start' : Qt.cyan, 'target' : Qt.yellow, 'checked' : Qt.red}
    
    def __init__(self, node, app):
        super(Tile, self).__init__()

        self.node = node
        self.subtext = ''

        self.type = 'clear'
        self._color = self._colors[self.type]

        self.app = app

        self.mousePressEvent = self.clicked


    # Set the text on the tile. Is used to display the distance to the target
    def set_subtext(self, text):
        self.subtext = text


    def paint(self, painter, options, widget):
        painter.setBrush(self._color)
        if self.node.checked and self.type == 'clear':
            painter.setBrush(self._colors['checked'])
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRect(self.node.x*self.size, self.node.y*self.size, self.size, self.size)


    def boundingRect(self):
        return QRectF(self.node.x*self.size, self.node.y*self.size, self.size, self.size)


    # Called when the tile is clicked
    @pyqtSlot()
    def clicked(self, e):
        new_type = None
        if e.button() == Qt.LeftButton:
            self.node.enabled = not self.node.enabled
            new_type = 'clear' if self.node.enabled else 'wall'
        elif e.button() == Qt.RightButton:
            self.node.enabled = True
            new_type = 'start'
        elif e.button() == Qt.MidButton:
            self.node.enabled = True
            new_type = 'target'
        if new_type is not None:
            self.set_type(new_type)


    def set_type(self, new_type):
        self.type = new_type
        self._color = self._colors[self.type]
        self.app.update_tiles(self)


