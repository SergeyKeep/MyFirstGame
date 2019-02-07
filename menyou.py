import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton
import mygame

# Наследование от QMainWindow, т.е. от главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText("Приветствую, ...")
        self.label.move(10, 0)

        self.name_label = QLabel(self)
        self.name_label.setText("Введите имя: ")
        self.name_label.move(10, 13)

        self.name_input = QLineEdit(self)
        self.name_input.move(10, 35)

        self.btn0 = QPushButton('сохранить', self)
        self.btn0.move(110, 80)
        self.btn0.resize(self.btn0.sizeHint())
        self.btn0.clicked.connect(self.hello)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Звездные войны")  # заголовок окна

        self.button_1 = QPushButton(self)
        self.button_1.move(110, 50)
        self.button_1.setText("Запуск")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(110, 20)
        self.button_2.setText("Выход")
        self.button_2.clicked.connect(self.run_2)
        self.show()

    def hello(self):
        self.name = self.name_input.text()
        self.label.setText("Привет, {}".format(self.name))

    def run(self):
        mygame.run_game()

    def run_2(self):
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())