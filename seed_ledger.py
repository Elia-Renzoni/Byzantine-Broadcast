import socket
import json

net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def join_cluster(local_address, seed_address):
    if seed_address is None:
        return False
    net.connect(seed_address)
    join_request = {
            "body": local_address,
            "hash": hash(local_address),
            "id": "join",
    }
    net.send(json.dumps(join_request))
    reply = net.recv(4048)

    # TODO-> check timeout and add simple retry mechanism
    
