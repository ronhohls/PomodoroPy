from PyQt6.QtWidgets import QApplication
from ui import PomodoroUI

if __name__ == '__main__':
    app = QApplication([])
    window = PomodoroUI()
    window.show()
    app.exec()
