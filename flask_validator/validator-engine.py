class ValidatorEngine():

    @staticmethod
    def required(data):
        if data is None or len(data) == 0:
            return False
        return True

    @staticmethod
    def max(data, value):
        if data > len(value):
            return False
        return True


engine = {
    'required': ValidatorEngine.required,
    'max': ValidatorEngine.max
}


if __name__ == '__main__':
    pass