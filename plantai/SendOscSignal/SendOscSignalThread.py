import time
import csv
import random
from threading import Thread


class SendOscSignalThread(Thread):
    def __init__(self, name: str) -> None:
        Thread.__init__(self)
        self.seconds = 10
        self.running = False
        self.checked = True
        self.name = name
        self.stop_thread = False

        self.mock_data = []

        with open(f'plantai/mockData/{name}.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.mock_data.append(row)

    def run(self) -> None:
        while True:
            if self.running and self.checked:
                print(f'{self.name}, {random.choice(self.mock_data)}')
            if self.stop_thread:
                break
            time.sleep(self.seconds)
