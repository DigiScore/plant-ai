import sys

from PySide6 import QtWidgets

from interface.MainWindow import Ui_MainWindow
from SendOscSignal.SendOscSignalThread import SendOscSignalThread


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.running = False
        # start
        self.start_pause_button.clicked.connect(self.start_pause_button_clicked)

        self.threads = [SendOscSignalThread('plant1'),
                        SendOscSignalThread('plant2'),
                        SendOscSignalThread('plant3'),
                        SendOscSignalThread('plant4'),
                        SendOscSignalThread('plant5'),
                        SendOscSignalThread('plant6')]
        for plant in self.threads:
            plant.start()

    def start_pause_button_clicked(self):
        self.running = not self.running
        if self.running:
            self.start_pause_button.setText("Pause")
        else:
            self.start_pause_button.setText("Start")

        for plant in self.threads:
            plant.running = self.running


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
