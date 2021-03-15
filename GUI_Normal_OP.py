#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt5.QtWidgets import QListWidget, QComboBox, QFileDialog, QMessageBox
from PIL import Image, ImageTk
import os.path

from Normal_OP import strength_normal_list

def popup_dialog(txt):
    msg = QMessageBox()
    msg.setText(txt)
    msg.exec_()

def strength_normals(url_list, folder_dir):
    popup_dialog('Processing...')
    normal_list = [ os.path.normpath(x.path()) for x in url_list ]
    
    strength_normal_list(normal_list, folder_dir)
    popup_dialog('Finished!')


class DnDWindow(QWidget):
    def __init__(self):
        # Basic widget config
        super().__init__()
        # For Drag n drops
        self.setAcceptDrops(True)

        self.line_edit = None

    def dropEvent(self, event):
        # For the nature of the widget we just take the first
        # element
        strength_normals(event.mimeData().urls(), self.line_edit.text())

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


def options_dialog_GUI(app):
    main_window = DnDWindow()
    dir_edit = QLineEdit()

    main_window.line_edit = dir_edit

    grid = QGridLayout()

    # Button events
    def origin_search():
        filename = QFileDialog.getExistingDirectory(None, "Open Folder", '.')
        if filename:
            dir_edit.setText(filename)

    search_button = QPushButton('Search')
    search_button.clicked.connect(origin_search)

    grid.addWidget(QLabel('Origin Resource pack:    '), 1, 0)
    grid.addWidget(dir_edit, 2, 0)
    grid.addWidget(search_button, 2, 1)
    grid.addWidget(QLabel('     '), 2, 0)
    grid.addWidget(QLabel('     '), 3, 0)
    grid.addWidget(QLabel('     '), 4, 0)
    grid.addWidget(QLabel('      Drag here the files  '), 5, 0)
    grid.addWidget(QLabel('     '), 6, 0)
    grid.addWidget(QLabel('     '), 7, 0)
    grid.addWidget(QLabel('     '), 8, 0)

    main_window.setLayout(grid)
    main_window.show()
    app.exec()

if __name__ == '__main__':
    app = QApplication([])
    options_dialog_GUI(app)
    