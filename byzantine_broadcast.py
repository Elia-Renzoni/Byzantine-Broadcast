import socket
import json

class ByzantineFault:
    def __init__(self):
        self.acks = 0

    def add_ack(self):
        self.acks += 1

    def is_byzantine_quorum_reached(self):
        return (self.acks + 3) / 2
        

def send_to(peer_address, message):
    net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net.connect(peer_address)

    net.send(message)
    data = net.recv(2048)
    return json.load(data)

def perform_checksum(checksum):
    pass
