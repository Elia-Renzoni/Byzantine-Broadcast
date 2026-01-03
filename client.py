import socket
import sys
import json

if __name__ == '__main__':
    net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net.connect((sys.argv[0], sys.argv[1]))

    payload = {
            "body": "foo-bar",
            "hash": hash("foo-bar"),
            "id": "msg"
    }
    data = json.dumps(payload)
    net.send(data)

    res = net.recv(4048)
    print(res)
    net.close()
