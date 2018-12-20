import re


class Date(object):

    rules = {
            'd': '1-31',
            'D': '01-31',
            'M': '01-12',
            'm': '1-12',
            'y': '2',
            'Y': '4',
            'h': '00-23',
            'i': '00-59',
            's': '00-59'
    }

    def _build_regex(self, format):
        date_format_string, time_format_string = format.split(' ')
        time_regex_string= self._time_regex_string(time_format_string)
        date_regex_string = self._date_regex_string(date_format_string)
        return  '%s %s'%(date_regex_string, time_regex_string)

    def _time_regex_string(self, time_format_string):
        if ':' not in time_format_string:
            raise KeyError('Invalid time splitter use :')

        time_format_data = time_format_string.split(':')
        time_format = []
        for data in time_format_data:
            rule = Date.rules.get(data, None)
            if not rule: 
                raise KeyError('Invalid time splitter use :')
            time_format.append('[%s]{2}'%(rule))
        return  r'[:]'.join(time_format)

    def _date_regex_string(self, date_format_string):
        splitters = ['-', '/']
        date_splitter = ''
        date_format = []
        for splitter in splitters:
            if splitter in date_format_string:
                date_splitter = splitter
                date_format_data = date_format_string.split(splitter)

        if not date_splitter:
            raise KeyError('Invalid date splitter use \\ or -')

        for data in date_format_data:
            rule  = Date.rules.get(data, None)
            if not rule:
                raise KeyError('Invalid date splitter \\ or -')

            if data == 'y' or data == 'Y':
                date_format.append('\\d{%s}'%(rule))
            else:
                date_format.append('[%s]{1,2}'%(rule))

        return ('[%s]'%(date_splitter)).join(date_format)

    @staticmethod
    def date(request_data, date_format=None):
        error_msg = 'This field must be a date that match this format {arg}'\
            .format(arg=date_format)
        regex_rule = Date()._build_regex(date_format)
        regex = re.compile(regex_rule)
        result = regex.match(request_data)
        print(request_data, date_format, regex_rule)
        if not result:
            return {'status': False, 'message': error_msg}

        return {'status': True}

