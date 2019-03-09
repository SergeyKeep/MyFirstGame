from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self, count):
        QMainWindow.__init__(self)
        super().__init__()
        self.count = count
        self.initUI()
    def initUI(self):
        self.start_layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText("Game Over...")

        self.name_label = QLabel(self)
        self.name_label.setText("Ваш счет в игре: " + str(self.count))
        self.name_label.move(0, 15)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())