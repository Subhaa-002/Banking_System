class InsufficientFundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidAccountException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OverDraftLimitExceededException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
