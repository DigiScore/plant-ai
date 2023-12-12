import sys

from PySide6 import QtWidgets

from interface.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.running = False
        # start
        self.start_pause_button.clicked.connect(self.start_pause_button_clicked)

    def start_pause_button_clicked(self):
        self.running = not self.running
        print(self.running)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
