from PySide6.QtWidgets import QApplication
import sys
from ui import MainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())