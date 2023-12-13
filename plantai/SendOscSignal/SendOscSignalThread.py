import time
import csv
from pathlib import Path
from threading import Thread


class SendOscSignalThread(Thread):
    def __init__(self, name: str) -> None:
        Thread.__init__(self)
        self.seconds = 10
        self.running = False
        self.checked = True
        self.name = name

        self.mock_data = []

        with open(f'plantai/mockData/{name}.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.mock_data.append(row)

    def run(self) -> None:
        while True:
            if self.running and self.checked:
                print(f'running {self.name}')
            else:
                print(f'paused {self.name}')
            time.sleep(self.seconds)
