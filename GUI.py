#####
# For next commit:
# - Show at least first image
# - Develop move_pic function
####

import glob     # to get all files inside a folder
import os
from PySide import QtCore, QtGui, QtUiTools


class UI:
    def __init__(self, file_path):
        self.ui = self.load_ui_widget(file_path)

        # to become folder paths
        self.source_path = ''
        self.left_path = ''
        self.right_path = ''

        self.files_in_source = list()  # list with all files inside source folder

        self.initialize()   # connect buttons with actions

    # Load a GUI from a .ui file function
    @staticmethod
    def load_ui_widget(file_path):
        loader = QtUiTools.QUiLoader()       # file loader
        ui_file = QtCore.QFile(file_path)    # file object
        ui_file.open(QtCore.QFile.ReadOnly)
        ui = loader.load(ui_file, None)      # load file into ui object
        ui_file.close()
        return ui

    # Function to initialise ui, connecting all buttons and actions
    def initialize(self):
        self.ui.button_source.clicked.connect(lambda: self.button_press('source'))  # button source will with get_path
        self.ui.button_left.clicked.connect(lambda: self.button_press('left'))
        self.ui.button_right.clicked.connect(lambda: self.button_press('right'))

    def button_press(self, sender):
        # source will always modify source folder path
        if sender == 'source':
            self.source_path = QtGui.QFileDialog.getExistingDirectory()  # select folder dialog
            os.chdir(self.source_path)      # go to source folder
            self.files_in_source = glob.glob("*.jpg")   # get all files inside source folder

            for file in self.files_in_source:
                print(os.path.join(self.source_path, file))

        # left button case:
        elif sender == 'left':
            if self.left_path == '':    # if left_path is empty, then assign a path to it
                self.left_path = QtGui.QFileDialog.getExistingDirectory()
                print("left path is:", self.left_path)
            else:   # if it isn't, move or copy picture to it
                self.move_pic('left')

        # right button case:
        elif sender == 'right':
            if self.right_path == '':    # if right_path is empty, then assign a path to it
                self.right_path = QtGui.QFileDialog.getExistingDirectory()
                print("right path is:", self.right_path)
            else:   # if it isn't, move or copy picture to it
                self.move_pic('right')

    def move_pic(self, direction):
        print("Moving current picture to the", direction)   # pretend something's happening

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)  # create application
    main_window = UI("main_window.ui")  # define main_window as the UI
    main_window.ui.show()
    sys.exit(app.exec_())
