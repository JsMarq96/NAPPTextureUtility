#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt5.QtWidgets import QListWidget, QComboBox, QFileDialog, QMessageBox
from PIL import Image, ImageTk
from os import path
import time
from Napp_Gen import generate_resourcepacks
from Splitter_GUI import splitter_GUI

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
        self.setText(event.mimeData().urls()[0].path())

    def dropeEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


#def image_compress_GUI(window):
compr_result = 'None'
pack_res = 1024
compress_list = []
list_view = None

def popup_dialog(txt):
    msg = QMessageBox()
    msg.setText(txt)
    msg.exec_()

def options_dialog_GUI(window):
    grid = QGridLayout()

    resolution_input = QLineEdit()
    compression_picker = QComboBox()
    compression_picker.addItems(['None', 'Light', 'Hard', 'Light w/Hard Speculars'])

    grid.addWidget(QLabel('Destination pack resolution:'), 0, 0)
    grid.addWidget(QLabel('Compression Levels:'), 0, 3)

    grid.addWidget(resolution_input, 1, 0)
    grid.addWidget(compression_picker, 1, 3)

    #Button events
    def add_compression():
        global compr_result, pack_res, list_view
        compr_result = compression_picker.currentText()
        pack_res = resolution_input.text()
        tmp = str(pack_res) + '-' + compr_result
        compress_list.append((pack_res, compr_result))
        list_view.addItem(tmp)
        window.close()

    add_button = QPushButton('Add')
    add_button.clicked.connect(add_compression)

    grid.addWidget(add_button, 2, 2)

    window.setLayout(grid)


def main_GUI(window):
    global list_view
    grid = QGridLayout()

    origin_input = DnDLineEdit()
    result_input = DnDLineEdit()
    pack_version_input = QLineEdit()

    list_view = QListWidget()

    origin_search_button = QPushButton('Search')
    result_search_button = QPushButton('Search')
    add_compress_button = QPushButton('Add resolution')
    scale_button = QPushButton('Scale')
    scale_zip_button = QPushButton('Scale and Zip')

    # Button events
    def origin_search():
        filename, _ = QFileDialog.getOpenFileName(None, "Open Folder", '.', "")
        if filename:
            origin_input.setText(filename)

    def result_search():
        filename, _ = QFileDialog.getOpenFileName(None, "Open Folder", '.', "")
        if filename:
            result_input.setText(filename)

    def add_resolution():
        res_window = QWidget()
        options_dialog_GUI(res_window)
        res_window.show()

    def resize():
        scale_button.setEnabled(False)
        scale_zip_button.setEnabled(False)

        popup_dialog('Processing...')

        generate_resourcepacks(origin_input.text(), compress_list, result_input.text(), pack_version_input.text())

        scale_button.setEnabled(True)
        scale_zip_button.setEnabled(True)

        popup_dialog('Finished!')

    def resize_zip():
        scale_button.setEnabled(False)
        scale_zip_button.setEnabled(False)

        popup_dialog('Processing...')

        generate_resourcepacks(origin_input.text(), compress_list, result_input.text(), pack_version_input.text(), True)

        scale_button.setEnabled(True)
        scale_zip_button.setEnabled(True)

        popup_dialog('Finished!')

    
    origin_search_button.clicked.connect(origin_search)
    result_search_button.clicked.connect(result_search)
    add_compress_button.clicked.connect(add_resolution)
    scale_button.clicked.connect(resize)
    scale_zip_button.clicked.connect(resize_zip)

    # First col
    grid.addWidget(QLabel('Origin Resource pack:'), 1,0)
    grid.addWidget(origin_input, 2, 0)
    grid.addWidget(origin_search_button, 2, 1)
    grid.addWidget(QLabel('Resource pack version:'), 5, 0)
    grid.addWidget(pack_version_input, 6, 0)

    # Second col
    grid.addWidget(QLabel('Result Pack Direction:'), 1, 3)
    grid.addWidget(result_input, 2, 3)
    grid.addWidget(result_search_button, 2, 4)
    grid.addWidget(QPushButton('Convert a single image'), 5, 4)

    # Third col
    grid.addWidget(QPushButton('Texture splitter'), 2, 6)
    grid.addWidget(add_compress_button, 3, 6)
    grid.addWidget(list_view, 4, 6)
    grid.addWidget(scale_button, 5, 6)
    grid.addWidget(scale_zip_button, 6, 6)

    window.setLayout(grid)


if __name__ == '__main__':
    app = QApplication([])
    main_window = QWidget()

    main_GUI(main_window)
    #options_dialog_GUI(main_window)

    main_window.show()
    app.exec()
