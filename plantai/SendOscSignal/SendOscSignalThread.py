import time
from threading import Thread


class SendOscSignalThread(Thread):
    def __init__(self, name: str):
        Thread.__init__(self)
        self.seconds = 1
        self.running = False

    def run(self):
        while True:
            if self.running:
                pass
            time.sleep(self.seconds)
