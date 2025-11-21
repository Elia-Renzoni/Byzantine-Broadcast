
class Request:
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

class Response:
    def __init__(self, status, content, checksum):
        self.execution_status = status
        self.response_content = content
        self.checksum = checksum

    def get_response_status(self):
        return self.execution_status

    def get_response_content(self):
        return self.response_content

    def get_response_checksum(self):
        return self.checksum


