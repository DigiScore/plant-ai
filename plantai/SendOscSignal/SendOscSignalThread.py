import time
from threading import Thread


class SendOscSignalThread(Thread):
    def __init__(self, name: str) -> None:
        Thread.__init__(self)
        self.seconds = 10
        self.running = False
        self.checked = True
        self.name = name

    def run(self) -> None:
        while True:
            if self.running and self.checked:
                print(f'running {self.name}')
            else:
                print(f'paused {self.name}')
            time.sleep(self.seconds)
