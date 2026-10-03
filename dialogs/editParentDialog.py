from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QInputDialog,
    QListView,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)


class EditParentDialog(QDialog):
    """
    @brief Диалог управления записями родительской таблицы.
    @details Позволяет просматривать, добавлять, изменять и удалять записи.
    """

    def __init__(self, data_controller, table, column, title, parent=None):
        super().__init__(parent)

        self.dataController = data_controller
        self.table = table
        self.column = column

        self.setWindowTitle(title)
        self.resize(400, 400)

        self.listView = QListView()
        self.model = QStringListModel(self)
        self.listView.setModel(self.model)

        self.addButton = QPushButton("Add")
        self.editButton = QPushButton("Edit")
        self.deleteButton = QPushButton("Delete")

        self.editButton.setEnabled(False)
        self.deleteButton.setEnabled(False)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.editButton)
        buttonLayout.addWidget(self.deleteButton)

        layout = QVBoxLayout(self)
        layout.addWidget(self.listView)
        layout.addLayout(buttonLayout)
        layout.addWidget(buttons)

        self.addButton.clicked.connect(self._add)
        self.editButton.clicked.connect(self._edit)
        self.deleteButton.clicked.connect(self._delete)
        self.listView.selectionModel().selectionChanged.connect(
            self._update_buttons
        )

        self._load_values()

    def _load_values(self):
        """
        @brief Загружает записи родительской таблицы.
        @details Обновляет модель QListView актуальным содержимым базы данных.
        """

        values = self.dataController.load_parent_values(
            self.table,
            self.column,
        )

        self.model.setStringList([value for _, value in values])

    def _selected_value(self):
        """
        @brief Возвращает выбранное значение.
        @details Если запись не выбрана, возвращается None.
        """

        index = self.listView.currentIndex()

        if not index.isValid():
            return None

        return index.data(Qt.ItemDataRole.DisplayRole)

    def _update_buttons(self):
        """
        @brief Обновляет состояние кнопок управления.
        @details Кнопки редактирования и удаления доступны только при выборе записи.
        """

        selected = self.listView.currentIndex().isValid()

        self.editButton.setEnabled(selected)
        self.deleteButton.setEnabled(selected)

    def _add(self):
        """
        @brief Добавляет новую запись.
        @details Значение вводится пользователем и сохраняется в родительской таблице.
        """

        value, accepted = QInputDialog.getText(
            self,
            "Add value",
            "Value:",
        )

        if not accepted:
            return

        value = value.strip()

        if not value:
            return

        try:
            self.dataController.add_parent_value(
                self.table,
                self.column,
                value,
            )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Database error",
                f"Failed to add value:\n{error}",
            )
            return

        self._load_values()

    def _edit(self):
        """
        @brief Изменяет выбранную запись.
        @details Изменяется только значение записи, её идентификатор сохраняется.
        """

        index = self.listView.currentIndex()

        if not index.isValid():
            return

        old_value = index.data(Qt.ItemDataRole.DisplayRole)

        value, accepted = QInputDialog.getText(
            self,
            "Edit value",
            "Value:",
            text=old_value,
        )

        if not accepted:
            return

        value = value.strip()

        if not value:
            return

        if value == old_value:
            return

        try:
            self.dataController.update_parent_value(
                self.table,
                self.column,
                old_value,
                value,
            )
        except Exception as error:
            QMessageBox.critical(
                self,
                "Database error",
                f"Failed to update value:\n{error}",
            )
            return

        self._load_values()

    def _delete(self):
        """
        @brief Удаляет выбранную запись.
        @details PostgreSQL с ON DELETE RESTRICT отклонит удаление записи,
        если на неё ссылаются записи таблицы main.
        """

        index = self.listView.currentIndex()

        if not index.isValid():
            return

        value = index.data(Qt.ItemDataRole.DisplayRole)

        answer = QMessageBox.question(
            self,
            "Delete value",
            f"Delete \"{value}\"?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        try:
            self.dataController.delete_parent_value(
                self.table,
                self.column,
                value,
            )
        except Exception as error:
            QMessageBox.warning(
                self,
                "Cannot delete value",
                "This value is used by existing contacts and cannot be deleted.",
            )
            return

        self._load_values()
