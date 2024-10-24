import time

class PomodoroTimer:
    def __init__(self):
        self.pomodoro_length = 25 * 60  # default 25 minutes
        self.short_break = 5 * 60  # default 5 minutes
        self.long_break = 15 * 60  # default 15 minutes
        self.pomodoro_count = 4  # default 4 pomodoros
        self.current_pomodoro = 0
        self.timer_running = False

    def set_pomodoro_length(self, minutes):
        self.pomodoro_length = minutes * 60

    def set_short_break(self, minutes):
        self.short_break = minutes * 60

    def set_long_break(self, minutes):
        self.long_break = minutes * 60

    def set_pomodoro_count(self, count):
        self.pomodoro_count = count

    def start_timer(self):
        self.timer_running = True
        self.current_pomodoro = 0
        while self.timer_running and self.current_pomodoro < self.pomodoro_count:
            self.run_pomodoro()
            if self.current_pomodoro < self.pomodoro_count:
                self.run_break()
            self.current_pomodoro += 1

    def stop_timer(self):
        self.timer_running = False

    def run_pomodoro(self):
        print(f'Starting pomodoro {self.current_pomodoro + 1}')
        self.run_timer(self.pomodoro_length)
        print(f'Pomodoro {self.current_pomodoro + 1} finished')

    def run_break(self):
        if (self.current_pomodoro + 1) % self.pomodoro_count == 0:
            print('Starting long break')
            self.run_timer(self.long_break)
            print('Long break finished')
        else:
            print('Starting short break')
            self.run_timer(self.short_break)
            print('Short break finished')

    def run_timer(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            if not self.timer_running:
                break
            time.sleep(1)
