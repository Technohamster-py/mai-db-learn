from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui.ui_main_window import Ui_MainWindow
from phoneBookModel import PhoneBookModel
from dataController import DataController


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dataController = DataController()

        self.phoneBookModel = PhoneBookModel(self.dataController.load_users(), self)
        self.ui.resultView.setModel(self.phoneBookModel)

        self._load_combo_boxes()
        self._connect_signals()

    def _load_combo_boxes(self):
        """
        @brief Заполняет ComboBox значениями из родительских таблиц БД.
        """

        self.ui.FirstnameCombo.addItem("")
        self.ui.FirstnameCombo.addItems(
            self.dataController.load_firstnames()
        )

        self.ui.LastnameCombo.addItem("")
        self.ui.LastnameCombo.addItems(
            self.dataController.load_lastnames()
        )

        self.ui.SurnameCombo.addItem("")
        self.ui.SurnameCombo.addItems(
            self.dataController.load_surnames()
        )

        self.ui.StreetCombo.addItem("")
        self.ui.StreetCombo.addItems(
            self.dataController.load_streets()
        )

    def _connect_signals(self):
        """
        @brief Подключает сигналы элементов интерфейса.
        """

        self.ui.searchButton.clicked.connect(self._search)
        self.ui.pushButton.clicked.connect(self._reset)

    def _search(self):
        """
        @brief Выполняет поиск записей по значениям формы.
        @details Все заполненные поля объединяются условием AND.
        """

        users = self.dataController.search_users(
            first_name=self.ui.FirstnameCombo.currentText(),
            last_name=self.ui.LastnameCombo.currentText(),
            surname=self.ui.SurnameCombo.currentText(),
            street=self.ui.StreetCombo.currentText(),
            phone=self.ui.phoneEdit.text().strip(),
        )

        if not users:
            QMessageBox.information(
                self,
                "Search",
                "No records found.",
            )
            return

        self.phoneBookModel.setUsers(users)

    def _reset(self):
        """
        @brief Сбрасывает параметры поиска и восстанавливает полный список.
        """

        self.ui.FirstnameCombo.setCurrentIndex(0)
        self.ui.LastnameCombo.setCurrentIndex(0)
        self.ui.SurnameCombo.setCurrentIndex(0)
        self.ui.StreetCombo.setCurrentIndex(0)
        self.ui.phoneEdit.clear()

        self.phoneBookModel.setUsers(
            self.dataController.load_users()
        )