import pynotify

class Alerter(object):
    def __init__(self):
        self.enabled = pynotify.init ("icon-summary-body")
        if not self.enabled:
            warn("Alerter failed to be initialized. No system alerts will be sent.")
    def alert(self, text):
        if not self.enabled:
            return
        notification = pynotify.Notification ("Pomodoro", text, "notification-message-im")
        notification.show()
