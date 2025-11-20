import threading

class CommitLog:
    def __init__(self):
        self.log = list()
        self.lock = threading.Lock()

    def insert(self, log_message):
        try:
            self.lock.acquire()
            self.log.push(log_message)
        except:
            pass
        finally:
            self.lock.release()

    def get_last_log(self):
        try:
            self.lock.acquire()
            return self.log[0]
        except:
            pass
        finally:
            self.lock.release()

    def remove_log(self, log_index):
        try:
            self.lock.acquire()
            self.log.remove(log_index)
        except:
            pass
        finally:
            self.lock.release()

class LogEntry:
    def __init__(self, content, status):
        self.data = content
        self.commit_status = status

    def is_commited(self):
        return self.commit_status

    def force_commit(self):
        if self.commit_status is False:
            self.commit_status = True
