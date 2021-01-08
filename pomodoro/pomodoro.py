from .waiter import Waiter

class Pomodoro(object):
    second = 1
    minute = 60 * second
    length = 25 * minute
    def start(self, on_step=lambda min_left, sec_left: None, on_end=lambda completed: None):
        def step(time_left):
            left = int(time_left)
            on_step(left / self.minute, left % self.minute)
        waiter = Waiter(self.length, self.second, step, on_end)
        waiter.start()
        step(self.length)
        return waiter
