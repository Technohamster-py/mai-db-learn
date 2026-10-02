from PySide6 import QtCore
from PySide6.QtCore import Qt
from user import User


class PhoneBookModel(QtCore.QAbstractTableModel):
    COLUMNS = ["Last name", "First name", "Surname", "Phone number", "Street address", "House", "Building", "Apartment"]

    def __init__(self, users=None, parent=None):
        super().__init__(parent)
        self.users = users if users is not None else []

    def rowCount(self, index=QtCore.QModelIndex()):
        return len(self.users)

    def columnCount(self, index=QtCore.QModelIndex()):
        return len(self.COLUMNS)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section >= len(self.COLUMNS):
            return None
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.COLUMNS[section]

        return None

    def data(self, index=QtCore.QModelIndex(), role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.users):
            return None

        user: User = self.users[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            match index.column():
                case 0: return user.last_name
                case 1: return user.first_name
                case 2: return user.surname
                case 3: return user.phone
                case 4: return user.street_address
                case 5: return user.house
                case 6: return user.building
                case 7: return user.apartment

    def setUsers(self, users):
        """
        @brief Заменяет содержимое модели.
        @details QTableView уведомляется о полном изменении набора данных.
        """

        self.beginResetModel()
        self.users = users if users is not None else []
        self.endResetModel()
