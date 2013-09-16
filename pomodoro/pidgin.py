import dbus

class Pidgin(object):
    STATUS_OFFLINE = 1
    STATUS_AVAILABLE = 2
    STATUS_UNAVAILABLE = 3
    STATUS_INVISIBLE = 4
    STATUS_AWAY = 5
    STATUS_EXTENDED_AWAY = 6
    STATUS_MOBILE = 7
    STATUS_TUNE = 8
    def __init__(self):
        try:
            bus = dbus.SessionBus()
            obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
            self.bus = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")
        except Exception as e:
            warn("Exception initializing pidgin. Pidgin status changes are disabled")
            warn(e)
            self.bus = None
    def set_available(self, message):
        self._set_status(self.STATUS_AVAILABLE, message)
    def set_busy(self, message):
        self._set_status(self.STATUS_AWAY, message)
    def _set_status(self, status_id, message):
        if self.bus is None:
            return
        new_status = self.bus.PurpleSavedstatusNew("", status_id)
        self.bus.PurpleSavedstatusSetMessage(new_status, message)
        self.bus.PurpleSavedstatusActivate(new_status)
