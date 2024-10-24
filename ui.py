from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import QTimer
from pomodoro import PomodoroTimer

class PomodoroUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.pomodoro_timer = PomodoroTimer()

    def initUI(self):
        self.setWindowTitle('Pomodoro Timer')

        layout = QVBoxLayout()

        self.pomodoro_length_label = QLabel('Pomodoro Length (minutes):')
        self.pomodoro_length_input = QLineEdit()
        layout.addWidget(self.pomodoro_length_label)
        layout.addWidget(self.pomodoro_length_input)

        self.short_break_label = QLabel('Short Break (minutes):')
        self.short_break_input = QLineEdit()
        layout.addWidget(self.short_break_label)
        layout.addWidget(self.short_break_input)

        self.long_break_label = QLabel('Long Break (minutes):')
        self.long_break_input = QLineEdit()
        layout.addWidget(self.long_break_label)
        layout.addWidget(self.long_break_input)

        self.pomodoro_count_label = QLabel('Number of Pomodoros:')
        self.pomodoro_count_input = QLineEdit()
        layout.addWidget(self.pomodoro_count_label)
        layout.addWidget(self.pomodoro_count_input)

        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_timer)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)

        self.current_pomodoro_label = QLabel('Current Pomodoro: 0')
        layout.addWidget(self.current_pomodoro_label)

        self.setLayout(layout)

    def start_timer(self):
        pomodoro_length = int(self.pomodoro_length_input.text())
        short_break = int(self.short_break_input.text())
        long_break = int(self.long_break_input.text())
        pomodoro_count = int(self.pomodoro_count_input.text())

        self.pomodoro_timer.set_pomodoro_length(pomodoro_length)
        self.pomodoro_timer.set_short_break(short_break)
        self.pomodoro_timer.set_long_break(long_break)
        self.pomodoro_timer.set_pomodoro_count(pomodoro_count)

        self.pomodoro_timer.start_timer()
        self.update_current_pomodoro()

    def stop_timer(self):
        self.pomodoro_timer.stop_timer()

    def update_current_pomodoro(self):
        self.current_pomodoro_label.setText(f'Current Pomodoro: {self.pomodoro_timer.current_pomodoro}')

if __name__ == '__main__':
    app = QApplication([])
    window = PomodoroUI()
    window.show()
    app.exec()
