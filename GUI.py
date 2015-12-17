#####
# For next commit:
# - Create an unified class for ui
####


from PySide import QtCore, QtGui, QtUiTools


# Load a GUI from a .ui file function
def load_ui_widget(file_path):
    loader = QtUiTools.QUiLoader()       # file loader
    ui_file = QtCore.QFile(file_path)    # file object
    ui_file.open(QtCore.QFile.ReadOnly)
    ui = loader.load(ui_file, None)      # load file into ui object
    ui_file.close()
    return ui


# Function to initialise ui, connecting all buttons and actions
def main_window_init(ui):
    ui.button_source.clicked.connect(get_path)  # button source will react with get_path


def get_path():
    path = QtGui.QFileDialog.getExistingDirectory()  # select folder dialog
    print("Path:" + path)   # test. Print path

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)  # create application
    main_window = load_ui_widget("main_window.ui")  # call our function to load a UI
    main_window_init(main_window)   # initialise ui
    main_window.show()
    sys.exit(app.exec_())
