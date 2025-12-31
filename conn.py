
class Request:
    '''
    Request represent a TCP request sent from the client or peers
    in the cluster.
    '''
    def __init__(self, content, checksum, request_id):
        self.request_content = content
        self.request_checksum = checksum
        self.request_id = request_id

    def get_request_content(self):
        return self.request_content

    def get_request_checksum(self):
        return self.request_checksum

    def get_request_id(self):
        return self.request_id

class Conn: 
    '''
    Conn contains a TCP connection established with the replica.
    '''
    def __init__(self, net_interface, address, port):
        self.net = net_interface
        self.address = address
        self.port = port

    def get_interface(self):
        return self.net

    def get_address(self):
        return self.address

    def get_port(self):
        return self.port
