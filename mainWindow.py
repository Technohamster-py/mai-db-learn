from PySide6.QtWidgets import QMainWindow

import dataController
from ui.ui_main_window import Ui_MainWindow
from phoneBookModel import PhoneBookModel
from dataController import DataController


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dataController = DataController()

        users = self.dataController.load_users()

        self.phoneBookModel = PhoneBookModel(users, self)
        self.ui.resultView.setModel(self.phoneBookModel)