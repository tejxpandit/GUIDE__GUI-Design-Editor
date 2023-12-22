# Timed Function Execution (Non-Blocking)
# Author : Tej Pandit
# Date : Oct 2023

from threading import Timer

class RepeatedTimer:
    def __init__(self):
        self._timer     = None
        self.interval   = None
        self.function   = None
        self.args       = None
        self.kwargs     = None
        self.is_running = False

    def set_timer(self, interval, function, *args, **kwargs):
        if self.is_running:
            self.stop()
            self.is_running = False
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False