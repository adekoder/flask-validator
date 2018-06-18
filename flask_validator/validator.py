from functools import wraps
from flask import current_app, request, jsonify
from .validator_engine import engine
from .rulesplitter import ruleSplitter


class Validator(): 

    def __init__(self, app=None, db=None):
        self.app = app
        if app is not None and db is not  None:
            self.init_app(app,db)
    
    def init_app(self, app,db):
        pass

    
    def __call__ (self, validation_type, rules):
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                method = self.__getattribute__(validation_type)
                if(method(rules)):
                    return func(*args, **kwargs)
                else:
                    return jsonify(
                        status=False,
                        errors=self.errors
                    ), 422
            return inner_wrapper
        return wrapper
    
    def validate(self, data, validation_rules):
        self.errors = {}
        for field, rules in validation_rules.items():
            for rule in rules:
                validator_name, validator_arg = ruleSplitter(rule).values()
                validate = engine[validator_name](data.get(field, None), validator_arg)
                if not validate['status'] :
                    self.errors[field] = validate['msg']
                    break
           

    def json(self, rules):
        data = request.get_json(force=True)
        self.validate(data, rules)
        if self.errors:
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




