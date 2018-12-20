class ValidatorAttributeError(Exception):
    def __init__(self, exp, message):
        self.exp = exp
        self.message = message


class ValidatorKeyError(Exception):
    def __init__(self, exp, message):
        self.exp = exp
        self.message = message

class ValidationArgumentError(Exception):
    def __init__ (self, exp, message):
        self.exp = exp
        self.message = message