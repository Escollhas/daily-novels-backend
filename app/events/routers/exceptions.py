class RequestsException(Exception):
    def __init__(self, message: str):
        self.message = message


class BadRequestException(RequestsException):
    def __init__(self, message: str):
        super().__init__(message)
