import threading

class Cluster:
    def __init__(self):
        self.membership_list = set()
        self.mutex = threading.Lock()

    def add_node(self):
        pass

    def delete_node(self):
        pass

    def fetch_membership_list(self):
        return self.membership_list

class Node:
    def __init__(self):
        pass
