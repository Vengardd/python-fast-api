class ConnectionException(Exception):
    ...


class ConnectionAlreadyExists(ConnectionException):
    def __init__(self):
        self.status_code = 400
        self.detail = "Connection already exists"

class ConnectionNotFound(ConnectionException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Connection not found"

