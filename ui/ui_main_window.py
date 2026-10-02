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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 0))
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName(u"actionContact")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.FirstnameCombo = QComboBox(self.centralwidget)
        self.FirstnameCombo.setObjectName(u"FirstnameCombo")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.FirstnameCombo)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.SurnameCombo = QComboBox(self.centralwidget)
        self.SurnameCombo.setObjectName(u"SurnameCombo")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.SurnameCombo)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.LastnameCombo = QComboBox(self.centralwidget)
        self.LastnameCombo.setObjectName(u"LastnameCombo")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.LastnameCombo)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.StreetCombo = QComboBox(self.centralwidget)
        self.StreetCombo.setObjectName(u"StreetCombo")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.StreetCombo)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.phoneEdit = QLineEdit(self.centralwidget)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setMaxLength(12)
        self.phoneEdit.setPlaceholderText(u"+79161234567")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.phoneEdit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout_2.addWidget(self.searchButton)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.resultView = QTableView(self.centralwidget)
        self.resultView.setObjectName(u"resultView")
        self.resultView.setMinimumSize(QSize(600, 0))

        self.horizontalLayout.addWidget(self.resultView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 25))
        self.menuAdd = QMenu(self.menubar)
        self.menuAdd.setObjectName(u"menuAdd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdd.menuAction())
        self.menuAdd.addAction(self.actionContact)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionContact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lastname", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Street", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.phoneEdit.setInputMask("")
        self.phoneEdit.setText("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

