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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1045, 600)
        MainWindow.setMinimumSize(QSize(900, 0))
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName(u"actionContact")
        self.actionFirst_names = QAction(MainWindow)
        self.actionFirst_names.setObjectName(u"actionFirst_names")
        self.actionSurnames = QAction(MainWindow)
        self.actionSurnames.setObjectName(u"actionSurnames")
        self.actionLast_names = QAction(MainWindow)
        self.actionLast_names.setObjectName(u"actionLast_names")
        self.actionStreets = QAction(MainWindow)
        self.actionStreets.setObjectName(u"actionStreets")
        self.actionDelete_contact = QAction(MainWindow)
        self.actionDelete_contact.setObjectName(u"actionDelete_contact")
        self.actionEdit_contact = QAction(MainWindow)
        self.actionEdit_contact.setObjectName(u"actionEdit_contact")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.FirstnameCombo = QComboBox(self.widget)
        self.FirstnameCombo.setObjectName(u"FirstnameCombo")
        self.FirstnameCombo.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.FirstnameCombo)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.SurnameCombo = QComboBox(self.widget)
        self.SurnameCombo.setObjectName(u"SurnameCombo")
        self.SurnameCombo.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.SurnameCombo)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.LastnameCombo = QComboBox(self.widget)
        self.LastnameCombo.setObjectName(u"LastnameCombo")
        self.LastnameCombo.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.LastnameCombo)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.StreetCombo = QComboBox(self.widget)
        self.StreetCombo.setObjectName(u"StreetCombo")
        self.StreetCombo.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.StreetCombo)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.phoneEdit = QLineEdit(self.widget)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setMaximumSize(QSize(200, 16777215))
        self.phoneEdit.setMaxLength(12)
        self.phoneEdit.setPlaceholderText(u"+79161234567")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.phoneEdit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchButton = QPushButton(self.widget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_2.addWidget(self.searchButton)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.widget)

        self.resultView = QTableView(self.centralwidget)
        self.resultView.setObjectName(u"resultView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultView.sizePolicy().hasHeightForWidth())
        self.resultView.setSizePolicy(sizePolicy)
        self.resultView.setMinimumSize(QSize(700, 0))
        self.resultView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resultView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.resultView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.resultView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1045, 25))
        self.menuAdd = QMenu(self.menubar)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuAdd.addAction(self.actionContact)
        self.menuEdit.addAction(self.actionFirst_names)
        self.menuEdit.addAction(self.actionSurnames)
        self.menuEdit.addAction(self.actionLast_names)
        self.menuEdit.addAction(self.actionStreets)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEdit_contact)
        self.menuEdit.addAction(self.actionDelete_contact)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionContact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.actionFirst_names.setText(QCoreApplication.translate("MainWindow", u"First names", None))
        self.actionSurnames.setText(QCoreApplication.translate("MainWindow", u"Surnames", None))
        self.actionLast_names.setText(QCoreApplication.translate("MainWindow", u"Last names", None))
        self.actionStreets.setText(QCoreApplication.translate("MainWindow", u"Streets", None))
        self.actionDelete_contact.setText(QCoreApplication.translate("MainWindow", u"Delete contact", None))
#if QT_CONFIG(shortcut)
        self.actionDelete_contact.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit_contact.setText(QCoreApplication.translate("MainWindow", u"Edit contact", None))
#if QT_CONFIG(shortcut)
        self.actionEdit_contact.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
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
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

