# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.serachLayout = QVBoxLayout()
        self.serachLayout.setObjectName(u"serachLayout")
        self.FirstnameCombo = QComboBox(self.centralwidget)
        self.FirstnameCombo.setObjectName(u"FirstnameCombo")

        self.serachLayout.addWidget(self.FirstnameCombo)

        self.SurnameCombo = QComboBox(self.centralwidget)
        self.SurnameCombo.setObjectName(u"SurnameCombo")

        self.serachLayout.addWidget(self.SurnameCombo)

        self.LastnameCombo = QComboBox(self.centralwidget)
        self.LastnameCombo.setObjectName(u"LastnameCombo")

        self.serachLayout.addWidget(self.LastnameCombo)

        self.StreetCombo = QComboBox(self.centralwidget)
        self.StreetCombo.setObjectName(u"StreetCombo")

        self.serachLayout.addWidget(self.StreetCombo)

        self.phoneEdit = QLineEdit(self.centralwidget)
        self.phoneEdit.setObjectName(u"phoneEdit")

        self.serachLayout.addWidget(self.phoneEdit)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")

        self.serachLayout.addWidget(self.searchButton)


        self.horizontalLayout.addLayout(self.serachLayout)

        self.resultView = QTableView(self.centralwidget)
        self.resultView.setObjectName(u"resultView")

        self.horizontalLayout.addWidget(self.resultView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

