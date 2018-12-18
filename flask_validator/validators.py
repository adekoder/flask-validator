class Validators():
    @staticmethod
    def required(request_data, validation_arg=None):
        error_msg = 'This field is required'

        if request_data is None :
            return {'status': False, 'message': error_msg}
            
        if not isinstance(request_data, int):
            if len(request_data) == 0:
                return {'status': False, 'message': error_msg}
        
        return {'status': True}

    @staticmethod
    def max(request_data, validator_arg):
        error_msg = 'This field must not be greater than {args}'.format(
            args=validator_arg)
        if isinstance(request_data, int):
            if request_data > int(validator_arg):
                return { 'status': False, 'message': error_msg}
        else:
            if len(request_data) > int(validator_arg):
                return {'status': False, 'message': error_msg}
        return {'status': True}

    @staticmethod
    def min(request_data, validator_arg):
        error_msg = 'This field must not be less than {args}'.format(
            args=validator_arg)
        print(validator_arg)
        if isinstance(request_data, int):
            if request_data < int(validator_arg):
                return {'status': False, 'message': error_msg}
        else:
            if len(request_data) < int(validator_arg):
                return {'status': False, 'message': error_msg}
        return {'status': True}
    
    @staticmethod
    def alpha(request_data, validator_arg=None):
        error_msg = 'This field must contain on alphabets (A-Za-z)'
        if not request_data or  not request_data.isalpha()  :
            return {'status': False, 'message': error_msg}
        return {'status': True}

validators = {
    'required': Validators.required,
    'max': Validators.max,
    'min': Validators.min,
    'alpha': Validators.alpha
}
