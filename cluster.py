import threading

class Cluster:
    def __init__(self):
        self.membership_list = set()
        self.mutex = threading.Lock()

    def add_node(self, node):
        try:
            self.mutex.acquire()
            self.membership_list.add(node)
            return True
        except:
            return False
        finally:
            self.mutex.release()

    def delete_node(self, node):
        try:
            self.mutex.acquire()
            toDelete = None
            for peer in self.membership_list:
                _, addr = peer.get_fields()
                if addr == node:
                    toDelete = peer
                    break
            self.membership_list.remove(toDelete)
            return True
        except:
            return False
        finally:
            self.mutex.release()

    def fetch_membership_list(self):
        try:
            self.mutex.acquire()
            return self.membership_list
        except:
            pass
        finally:
            self.mutex.release()

class Node:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_fields(self):
        return [self.name, self.address]
