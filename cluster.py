import threading

class Cluster:
    def __init__(self):
        self.membership_list = set()
        self.mutex = threading.Lock()

    def add_node(self, node):
        pass

    def delete_node(self, nodeId):
        pass

    def fetch_membership_list(self):
        return self.membership_list

class Node:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_fields(self):
        return [self.name, self.address]
