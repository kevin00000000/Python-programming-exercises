class CustomException(Exception):
    def __init__(self, msg, num):
        self._msg = msg
        self._num = num
raise(CustomException('My Exception', 1024))