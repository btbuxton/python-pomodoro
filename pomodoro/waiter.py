import time
import threading

class Waiter(object):
    def __init__(self, total, increment, on_increment, on_end):
        self.total = total
        self.increment = increment
        self.on_increment = on_increment
        self.on_end = on_end
        self.active = False
       
    def start(self):
        self.active = True
        self.begin = time.time()
        self.end = self.begin + self.total
        self.each_increment()
        self.start_main_timer()
   
    def stop(self):
        self.main_timer.cancel()
        self.increment_timer.cancel()
        self.end_main_timer(False)
           
    def start_main_timer(self):
        timer = threading.Timer(self.total, lambda: self.end_main_timer(True))
        timer.daemon = True
        timer.start()
        self.main_timer = timer
       
    def end_main_timer(self, completed):
        self.active = False
        self.on_end(completed)
       
    def start_increment_timer(self):
        timer = threading.Timer(self.increment, self.each_increment)
        timer.daemon = True
        timer.start()
        self.increment_timer = timer
       
    def each_increment(self):
        if self.active:
            self.on_increment(self.end - time.time())
            self.start_increment_timer()
