import socket
import json

class ByzantineFault:
    def __init__(self, cluster_len):
        self.acks = 0
        self.byzantine_requirement = (cluster_len + 3) / 2

    def add_ack(self):
        self.acks += 1

    def is_byzantine_quorum_reached(self):
        return self.acks > self.byzantine_requirement

def send_to(peer_address, message):
    net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net.connect(peer_address)

    net.send(message)
    data = net.recv(2048)
    return json.load(data)

def check_hash(hash_value, to_hash):
   return hash(to_hash) == hash_value
