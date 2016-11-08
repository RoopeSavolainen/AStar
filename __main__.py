import sys

from ui import AStarApplication

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QGraphicsScene


def main():
    app = QApplication(sys.argv)
    app.quitOnLastWindowClosed = True
    
    window = AStarApplication()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

