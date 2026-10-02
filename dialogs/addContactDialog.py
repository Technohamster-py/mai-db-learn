from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)


class AddContactDialog(QDialog):
    """
    @brief Диалог добавления нового контакта.
    @details Позволяет выбрать существующие значения родительских таблиц
    или ввести новые значения, которые будут созданы при сохранении.
    """

    def __init__(self, data_controller, parent=None):
        super().__init__(parent)

        self.dataController = data_controller

        self.setWindowTitle("Add contact")

        self.firstNameCombo = QComboBox()
        self.lastNameCombo = QComboBox()
        self.surnameCombo = QComboBox()
        self.streetCombo = QComboBox()

        for combo in (
            self.firstNameCombo,
            self.lastNameCombo,
            self.surnameCombo,
            self.streetCombo,
        ):
            combo.setEditable(True)

        self.phoneEdit = QLineEdit()
        self.houseEdit = QLineEdit()
        self.buildingEdit = QLineEdit()
        self.apartmentEdit = QLineEdit()

        self._load_parent_values()

        formLayout = QFormLayout()
        formLayout.addRow("First name:", self.firstNameCombo)
        formLayout.addRow("Last name:", self.lastNameCombo)
        formLayout.addRow("Surname:", self.surnameCombo)
        formLayout.addRow("Street:", self.streetCombo)
        formLayout.addRow("Phone:", self.phoneEdit)
        formLayout.addRow("House:", self.houseEdit)
        formLayout.addRow("Building:", self.buildingEdit)
        formLayout.addRow("Apartment:", self.apartmentEdit)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(formLayout)
        layout.addWidget(buttons)

    def _load_parent_values(self):
        """
        @brief Загружает существующие значения родительских таблиц.
        """

        self.firstNameCombo.addItems(
            self.dataController.load_firstnames()
        )

        self.lastNameCombo.addItems(
            self.dataController.load_lastnames()
        )

        self.surnameCombo.addItems(
            self.dataController.load_surnames()
        )

        self.streetCombo.addItems(
            self.dataController.load_streets()
        )

    def get_data(self):
        """
        @brief Возвращает данные введённого контакта.
        """

        return {
            "first_name": self.firstNameCombo.currentText().strip(),
            "last_name": self.lastNameCombo.currentText().strip(),
            "surname": self.surnameCombo.currentText().strip(),
            "street": self.streetCombo.currentText().strip(),
            "phone": self.phoneEdit.text().strip(),
            "house": self.houseEdit.text().strip(),
            "building": self.buildingEdit.text().strip(),
            "apartment": self.apartmentEdit.text().strip(),
        }