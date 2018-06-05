from flask import current_app

class Validator(): 

    def __init__(self, app=None, db=None):
        self.app = app
        if app is not None and db is not  None:
            self.init_app(app,db)
    
    def init_app(self, app,db):
        pass
    




