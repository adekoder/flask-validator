from datetime import datetime

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
            try: 
                date_value_2 = datetime.strptime(args[1], args[0])
            except ValueError: 
                return {'status': False, 'message': error_msg}

            if date_value_1 != date_value_2 :
                error_msg += 'and value must be {arg}'.format(arg=args[1])
                return {'status': False, 'message': error_msg}
        
        return {'status': True}

    

