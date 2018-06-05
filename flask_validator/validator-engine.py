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
    
    

def ruleSpliter(rule):
    rule = rule.split(':')
    rule_field = rule[0]
    rule_data = rule[1].split(',')
    print(rule_field, rule_data)

engine = {
    'required': ValidatorEngine.required,
    'max': ValidatorEngine.max
}


if __name__ == '__main__':

    rule = 'max'
    data = 12

    validator_data  = rule.split(':')
    #print(engine['required'](data))
    #print(engine[validator_data[0]](data, validator_data[1]))
    print(ruleSpliter(rule))