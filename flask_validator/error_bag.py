from flask import request, jsonify, session, redirect
class ErrorBag():
    def __init__(self):
        self.errors = {}
    
    def response(self):
        return jsonify(
            status=False,
            errors=self.errors
        ), 422
        
    
    def addError(self, field, message):
        self.errors[field] = message
    
    def hasErrors(self):
        if self.errors:
            return True
        return False