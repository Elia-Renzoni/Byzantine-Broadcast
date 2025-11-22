import socket
import conn 
import threading
import json
import handlers

net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conns = list()
conn_mutex = threading.Lock()

def start_server(host, port):
    net.bind((host, port))
    net.listen()
    while True:
        client_conn, client_address = net.accept()
        t = threading.Thread(target=handle_request(conn.Conn(
            client_conn, 
            client_address[0], 
            client_address[1]
        )))
        t.start()

def handle_request(connection):
    race = add_conn(connection)
    if race is True:
        connection.get_interface.close()
        return

    data = connection.get_interface().recv(2048)
    parsed = json.load(data)
    req = conn.Request(parsed['body'], parsed['checksum'], parsed['id'])
    result = handlers.request_strainer(req)
    if result is True:
        ack("", connection.get_interface())
    else:
        nack("", connection.get_interface())
    delete_conn(connection)

def graceful_shutdown():
    try: 
        conn_mutex.acquire()
        for c in conns:
            c.get_interface().close()
    except:
        pass
    finally:
        conn_mutex.release()

def add_conn(connection):
    try:
        conn_mutex.acquire()
        conns.append(connection)
        return False
    except:
        return True
    finally:
        conn_mutex.release()

def delete_conn(connection):
    try:
        conn_mutex.acquire()
        for c in conns:
            if (c.get_address(), c.get_port()) == (connection.get_address(), connection.get_port()):
                    conns.remove(c)
                    break
    except:
        pass
    finally:
        conn_mutex.release()

def ack(msg, connection):
    pass

def nack(msg, connection):
    pass

if __name__ == "__main__":
    start_server()
