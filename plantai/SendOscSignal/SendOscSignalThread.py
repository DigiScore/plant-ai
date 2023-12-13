import time
import csv
import random
from threading import Thread
from pythonosc import udp_client
from pythonosc import osc_message_builder


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
                osc_sender = udp_client.UDPClient("localhost", 2222)
                msg = osc_message_builder.OscMessageBuilder(address=f"/{self.name}")
                msg.add_arg(random.choice(self.mock_data))
                osc_sender.send(msg.build())
                print(msg)
            if self.stop_thread:
                break
            time.sleep(self.seconds)
