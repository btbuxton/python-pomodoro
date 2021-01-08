import tkinter
import tkinter.font

from .pomodoro import Pomodoro

class App:
    def __init__(self, master):
        self.master = master

        font = tkinter.font.Font(
            family="Helvetica", size=50, weight=tkinter.font.BOLD)
        self.pomodoro_count_text = tkinter.StringVar()
        tkinter.Label(master, textvariable=self.pomodoro_count_text,
                      justify=tkinter.constants.CENTER).grid(row=0, columnspan=2)
        self.time_left = tkinter.StringVar()
        tkinter.Label(master, textvariable=self.time_left, font=font, width=5).grid(
            row=1, columnspan=2, sticky=tkinter.constants.W)

        self.start_text = tkinter.StringVar()
        self.start_button = tkinter.Button(
            master, textvariable=self.start_text, command=self.start_clicked)
        self.reset_button = tkinter.Button(
            master, text="Reset", command=self.reset_pomodoro_count)

        self.start_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

        self.reset_pomodoro_count()
        self.reset_time_left()
        self.start_text.set("Start")

    def update_pomodoro_count(self):
        self.pomodoro_count_text.set("%d completed" % self._pomodoro_count)
        if self._pomodoro_count == 0:
            self.reset_button.config(state=tkinter.constants.DISABLED)
        else:
            self.reset_button.config(state=tkinter.constants.ACTIVE)

    def increase_pomodoro_count(self):
        self._pomodoro_count += 1
        self.update_pomodoro_count()

    def reset_pomodoro_count(self):
        self._pomodoro_count = 0
        self.update_pomodoro_count()

    def reset_time_left(self):
        self.time_left.set("00:00")
        self.master.wm_title("Pomodoro")

    def start_clicked(self):
        self.start_text.set("Cancel")
        pomodoro = Pomodoro()
        stoppable = pomodoro.start(self.on_pomodoro_step, self.on_pomodoro_end)
        self.start_button.configure(
            command=lambda: self.cancel_clicked(stoppable))

    def on_pomodoro_step(self, min_left, sec_left):
        self.time_left.set("%02d:%02d" % (min_left, sec_left))
        self.master.wm_title(self.time_left.get())

    def on_pomodoro_end(self, completed):
        self.start_text.set("Start")
        self.start_button.configure(command=self.start_clicked)
        self.reset_time_left()
        if completed:
            self.increase_pomodoro_count()

    def cancel_clicked(self, stoppable):
        stoppable.stop()


def main():
    root = tkinter.Tk()
    root.wm_title("Pomodoro")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
