# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(288, 265)
        MainWindow.setMinimumSize(QSize(250, 265))
        MainWindow.setMaximumSize(QSize(288, 344))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.plant6_cb = QCheckBox(self.centralwidget)
        self.plant6_cb.setObjectName(u"plant6_cb")
        self.plant6_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant6_cb, 5, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.plant5_cb = QCheckBox(self.centralwidget)
        self.plant5_cb.setObjectName(u"plant5_cb")
        self.plant5_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant5_cb, 4, 2, 1, 1)

        self.plant1_cb = QCheckBox(self.centralwidget)
        self.plant1_cb.setObjectName(u"plant1_cb")
        self.plant1_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant1_cb, 0, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.plant4_cb = QCheckBox(self.centralwidget)
        self.plant4_cb.setObjectName(u"plant4_cb")
        self.plant4_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant4_cb, 3, 2, 1, 1)

        self.plant3_cb = QCheckBox(self.centralwidget)
        self.plant3_cb.setObjectName(u"plant3_cb")
        self.plant3_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant3_cb, 2, 2, 1, 1)

        self.start_pause_button = QPushButton(self.centralwidget)
        self.start_pause_button.setObjectName(u"start_pause_button")

        self.gridLayout.addWidget(self.start_pause_button, 7, 1, 1, 1)

        self.plant2_cb = QCheckBox(self.centralwidget)
        self.plant2_cb.setObjectName(u"plant2_cb")
        self.plant2_cb.setChecked(True)

        self.gridLayout.addWidget(self.plant2_cb, 1, 2, 1, 1)

        self.plant1_sb = QSpinBox(self.centralwidget)
        self.plant1_sb.setObjectName(u"plant1_sb")
        self.plant1_sb.setMaximum(1000)
        self.plant1_sb.setValue(10)

        self.gridLayout.addWidget(self.plant1_sb, 0, 1, 1, 1)

        self.plant2_sb = QSpinBox(self.centralwidget)
        self.plant2_sb.setObjectName(u"plant2_sb")
        self.plant2_sb.setMaximum(1000)
        self.plant2_sb.setValue(10)

        self.gridLayout.addWidget(self.plant2_sb, 1, 1, 1, 1)

        self.plant3_sb = QSpinBox(self.centralwidget)
        self.plant3_sb.setObjectName(u"plant3_sb")
        self.plant3_sb.setMaximum(1000)
        self.plant3_sb.setValue(10)

        self.gridLayout.addWidget(self.plant3_sb, 2, 1, 1, 1)

        self.plant4_sb = QSpinBox(self.centralwidget)
        self.plant4_sb.setObjectName(u"plant4_sb")
        self.plant4_sb.setMaximum(1000)
        self.plant4_sb.setValue(10)

        self.gridLayout.addWidget(self.plant4_sb, 3, 1, 1, 1)

        self.plant5_sb = QSpinBox(self.centralwidget)
        self.plant5_sb.setObjectName(u"plant5_sb")
        self.plant5_sb.setMaximum(1000)
        self.plant5_sb.setValue(10)

        self.gridLayout.addWidget(self.plant5_sb, 4, 1, 1, 1)

        self.plant6_sb = QSpinBox(self.centralwidget)
        self.plant6_sb.setObjectName(u"plant6_sb")
        self.plant6_sb.setMaximum(1000)
        self.plant6_sb.setValue(10)

        self.gridLayout.addWidget(self.plant6_sb, 5, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Plant AI", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plant 3 seconds", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plant 1 seconds", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Plant 4 seconds", None))
        self.plant6_cb.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plant 5 seconds", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plant 2 seconds", None))
        self.plant5_cb.setText("")
        self.plant1_cb.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Plant 6 seconds", None))
        self.plant4_cb.setText("")
        self.plant3_cb.setText("")
        self.start_pause_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.plant2_cb.setText("")
    # retranslateUi

