import sys
from threading import Lock, Thread

from PySide6 import QtWidgets

from interface.MainWindow import Ui_MainWindow
from SendOscSignal.SendOscSignalThread import SendOscSignalThread


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.threads = [SendOscSignalThread('plant1'),
                        SendOscSignalThread('plant2'),
                        SendOscSignalThread('plant3'),
                        SendOscSignalThread('plant4'),
                        SendOscSignalThread('plant5'),
                        SendOscSignalThread('plant6')]
        for plant in self.threads:
            plant.start()

        self.running = False
        self.start_pause_button.clicked.connect(self.start_pause_button_clicked)

        self.plant1_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 0))
        self.plant2_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 1))
        self.plant3_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 2))
        self.plant4_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 3))
        self.plant5_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 4))
        self.plant6_cb.stateChanged.connect(lambda i: self.checkbox_changed(i, 5))

        self.plant1_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 0))
        self.plant2_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 1))
        self.plant3_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 2))
        self.plant4_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 3))
        self.plant5_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 4))
        self.plant6_sb.valueChanged.connect(lambda i: self.spinbox_changed(i, 5))

    def checkbox_changed(self, state: int, number: int) -> None:
        self.threads[number].running = False if state == 0 else True

    def spinbox_changed(self, spinbox: int, number: int) -> None:
        self.threads[number].seconds = spinbox

    def start_pause_button_clicked(self) -> None:
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
