#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt5.QtWidgets import QListWidget

'''
    PyQt5 Line edit widget that adds drag n drop funcionality
'''
class DnDLineEdit(QLineEdit):
    def __init__(self, folders = False):
        # Basic widget config
        super().__init__()
        # For Drag n drops
        self.setAcceptDrops(True)
        self.file_url = ''
        self.accept_folders = folders

    def dropEvent(self, event):
        # For the nature of the widget we just take the first
        # element
        self.setText(event.mimeData().urls()[0].toString())

    def dropeEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


app = QApplication([])
window = QWidget()
grid = QGridLayout()

origin_input = DnDLineEdit()
result_input = DnDLineEdit()
pack_version_input = QLineEdit()

list_view = QListWidget()
# First col
grid.addWidget(QLabel('Origin Resource pack:'), 1,0)
grid.addWidget(origin_input, 2, 0)
grid.addWidget(QPushButton('Search'), 2, 1)
grid.addWidget(QLabel('Resource pack version:'), 5, 0)
grid.addWidget(pack_version_input, 6, 0)

# Second col
grid.addWidget(QLabel('Result Pack Direction:'), 1, 3)
grid.addWidget(result_input, 2, 3)
grid.addWidget(QPushButton('Search'), 2, 4)
grid.addWidget(QPushButton('Convert a single image'), 5, 4)

# Third col
grid.addWidget(QPushButton('Texture splitter'), 2, 6)
grid.addWidget(QPushButton('Add resolution'), 3, 6)
grid.addWidget(list_view, 4, 6)
grid.addWidget(QPushButton('Scale'), 5, 6)
grid.addWidget(QPushButton('Scale and Zip'), 6, 6)

window.setLayout(grid)
window.show()
app.exec()
