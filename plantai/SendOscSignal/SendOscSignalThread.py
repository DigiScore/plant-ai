import time
from threading import Thread


class SendOscSignalThread(Thread):
    def __init__(self, name: str) -> None:
        Thread.__init__(self)
        self.seconds = 10
        self.running = False
        self.name = name

    def run(self) -> None:
        while True:
            if self.running:
                print('running')
            time.sleep(self.seconds)
