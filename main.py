from PyQt6.QtWidgets import QApplication

from algoland import Algoland

if __name__ == '__main__':
    app = QApplication([])
    window = Algoland()
    window.show()
    app.exec()
