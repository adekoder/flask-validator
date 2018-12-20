from datetime import datetime
from ..exceptions import ValidationArgumentError

class Date(object):



    @staticmethod
    def date(request_data, *args):
        error_msg = 'This field must be a date that match this format {arg}'\
            .format(arg=args[0])
        try:  
            date_value_1 = datetime.strptime(request_data, args[0])
        except ValueError:
            print('here')
            return {'status': False, 'message': error_msg}

        if len(args) == 2:
            date_value_2 = datetime.strptime(args[1], args[0])
            if date_value_1 != date_value_2 :
                error_msg += 'and value must be {arg}'.format(arg=args[1])
                return {'status': False, 'message': error_msg}
        
        return {'status': True}
    
    @staticmethod
    def after(request_data, *args):
        if(len(args) != 2):
            raise ValidationArgumentError('ArgumentError', 'Usage should be date_after:<format>,<value>')
        
        error_msg = 'This field must be after this date {arg}'\
        .format(arg=args[0])
    
        try:
            date_value_1 = datetime.strptime(request_data, args[0])
        except ValueError:
            return {'status': False, 'message': \
                'This field must be a date that match this format'.format(arg=args[0])}
        
        date_value_2 = datetime.strptime(args[1], args[0])
        if not date_value_1 > date_value_2:
            return {'status': False, 'message': error_msg}
        
        return {'status': True}

    @staticmethod
    def after_or_equal(request_data, *args):
        if(len(args) != 2):
            raise ValidationArgumentError('ArgumentError', 'Usage should be date_after_or_equal:<format>,<value>')
        
        error_msg = 'This field must be after or equal to this date {arg}'\
        .format(arg=args[0])
    
        try:
            date_value_1 = datetime.strptime(request_data, args[0])
        except ValueError:
            return {'status': False, 'message': \
                'This field must be a date that match this format'.format(arg=args[0])}
        
        date_value_2 = datetime.strptime(args[1], args[0])
        if not date_value_1 >= date_value_2:
            return {'status': False, 'message': error_msg}
        
        return {'status': True}
        
    @staticmethod
    def before(request_data, *args):
        if(len(args) != 2):
            raise ValidationArgumentError('ArgumentError', 'Usage should be date_before:<format>,<value>')
        
        error_msg = 'This field must be before this date {arg}'\
        .format(arg=args[0])
    
        try:
            date_value_1 = datetime.strptime(request_data, args[0])
        except ValueError:
            return {'status': False, 'message': \
                'This field must be a date that match this format'.format(arg=args[0])}
        
        date_value_2 = datetime.strptime(args[1], args[0])
        if not date_value_1 < date_value_2:
            return {'status': False, 'message': error_msg}
        
        return {'status': True}
    
    @staticmethod
    def before_or_equal(request_data, *args):
        if(len(args) != 2):
            raise ValidationArgumentError('ArgumentError', 'Usage should be date_before_or_equal:<format>,<value>')
        
        error_msg = 'This field must be before or equal to this date {arg}'\
        .format(arg=args[0])
    
        try:
            date_value_1 = datetime.strptime(request_data, args[0])
        except ValueError:
            return {'status': False, 'message': \
                'This field must be a date that match this format'.format(arg=args[0])}
        
        date_value_2 = datetime.strptime(args[1], args[0])
        if not date_value_1 <= date_value_2:
            return {'status': False, 'message': error_msg}
        
        return {'status': True}


    

