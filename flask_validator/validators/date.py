from datetime import datetime

class Date(object):



    @staticmethod
    def date(request_data, date_format):
        error_msg = 'This field must be a date that match this format {arg}'\
            .format(arg=date_format)
        try:
            datetime.strptime(request_data, date_format)
        except ValueError:
            return {'status': False, 'message': error_msg}
        return {'status': True}

    @staticmethod
    def date_equals(request_data, validator_arg):
        error_msg = 'This field must be equal to'
        if request_data != validator_arg:
            return {'status': False, 'message': error_msg}
    

