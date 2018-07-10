import sys
import traceback
from functools import wraps
from flask import current_app, request, jsonify, session
from .validator_engine import engine
from .rulesplitter import ruleSplitter
from exceptions import ValidatorAttributeError, ValidatorKeyError
from error_bag import ErrorBag


class Validator(): 

    def __init__(self, app=None, db=None):
        self.app = app
        if app is not None and db is not  None:
            self.init_app(app,db)
    
    def init_app(self, app,db=None):
        self.app = app
        self.db = db

    
    def __call__ (self, validation_type, rules):
        def wrapper(func):
            @wraps(func)
            def inner_wrapper(*args, **kwargs):
                try:
                    validation_type_method = self.__getattribute__(validation_type)
                    if(validation_type_method(rules)):
                        return func(*args, **kwargs)
                    else:
                        return self.errors.response()
                except AttributeError:
                    raise ValidatorAttributeError('AttributeError', \
                        '''%s passed and expecting json or form_data or query_string or headers or files''' \
                        % (validation_type))
            return inner_wrapper
        return wrapper
    
    def validate(self, data, validation_rules):
        self.errors = ErrorBag()
        for field, rules in validation_rules.items():
            for rule in rules:
                validator_name, validator_arg = ruleSplitter(rule).values()
                try:
                    validate = engine[validator_name](data.get(field, None), validator_arg)
                except KeyError:
                    raise ValidatorKeyError(validator_name, 'Validator name is not known')
                if not validate['status'] :
                    self.errors.addError(field, validate['msg'])
                    break
           

    def json(self, rules):
        data = request.get_json(force=True)
        self.validate(data, rules)
        if self.errors.hasErrors():
            return False
        return True

    
    def form_data(self, rules):
        print('form_data')

    
    def query_string(self, rules):
        print('query_string')

   
    def headers(self, rules):
        print('headers')


    def files(self, rules):
        print('files')




if __name__ == "__main__":
    validator  = Validator()

    @validator('json', {
        'name': ['required', 'max:2'],
        'age': ['required', 'max:34'],
        'status': ['required']
    })
    def index():
        print('hello')

    print(index())




