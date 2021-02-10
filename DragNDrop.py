#!/usr/bin/env python3

from PyQt5.QWidgets import QMainWindow, QApplication

'''
    Temporary Drag n Drop widget using PyQt5
    TODO: Move the whole utility to PyQt5
    by Juan S. Marquerie
'''

class DragNDropWindow(QMainWindow):
    def __init__(self, folders = False):
        # Basic widget config
        super().__init__()
        self.setWindowTitle('Drop Here!')
        self.resize(200, 200)
        # For Drag n drops
        self.setAcceptDrops(True)
        self.file_url = ''
        self.accept_folders = folders

    def dropEvent(self, event):
        # For the nature of the widget we just take the first
        # element
        self.file_url = event.mineData().urls()[0]
        self.close()

    def dropeEvent(self, event):
        if event.mineData().hasUrls():
            event.accept()
        else:
            event.ignore()

'''
    Widget calling and response function
'''
def drag_n_drop_widget():
    wid_app = QApplication([])
    dnd_window = DragNDropWindow()
    dnd_window.show()
    wid_app.exec_()
    return dnd_window.file_url
