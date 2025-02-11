import sys
import sqlite3
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()
        self.pushButton.clicked.connect(self.add_edit_coffee)
        self.tableWidget.cellDoubleClicked.connect(self.edit_coffee)

    def load_data(self):
        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        coffee_data = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(coffee_data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки"])

        for row_index, row_data in enumerate(coffee_data):
            for col_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))

    def add_edit_coffee(self):
        self.add_edit_window = AddEditCoffeeForm(self)
        self.add_edit_window.show()

    def edit_coffee(self, row):
        coffee_id = self.tableWidget.item(row, 0).text()
        self.add_edit_window = AddEditCoffeeForm(self, coffee_id)
        self.add_edit_window.show()


class AddEditCoffeeForm(QtWidgets.QDialog):
    def __init__(self, parent, coffee_id=None):
        super().__init__(parent)
        try:
            uic.loadUi('addEditCoffeeForm.ui', self)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load UI: {e}")
            return

        self.coffee_id = coffee_id
        self.parent = parent

        if coffee_id:
            self.load_coffee_data()

        self.pushButton.clicked.connect(self.save_coffee_data)

    def load_coffee_data(self):
        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee WHERE id=?", (self.coffee_id,))
        coffee_data = cursor.fetchone()
        connection.close()

        if coffee_data:
            self.lineEditName.setText(coffee_data[1])
            self.lineEditRoast.setText(coffee_data[2])
            self.lineEditGround.setText(coffee_data[3])
            self.lineEditTaste.setText(coffee_data[4])
            self.lineEditPrice.setText(str(coffee_data[5]))
            self.lineEditVolume.setText(str(coffee_data[6]))

    def save_coffee_data(self):
        name = self.lineEditName.text()
        roast = self.lineEditRoast.text()
        ground = self.lineEditGround.text()
        taste = self.lineEditTaste.text()
        price = self.lineEditPrice.text()
        volume = self.lineEditVolume.text()

        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()

        if self.coffee_id:
            cursor.execute('''UPDATE coffee
                              SET name=?, roast_level=?, ground=?, taste_description=?, price=?, volume=?
                              WHERE id=?''', (name, roast, ground, taste, price, volume, self.coffee_id))
        else:
            cursor.execute('''INSERT INTO coffee (name, roast_level, ground, taste_description, price, volume)
                              VALUES (?, ?, ?, ?, ?, ?)''', (name, roast, ground, taste, price, volume))

        connection.commit()
        connection.close()

        self.parent.load_data()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
