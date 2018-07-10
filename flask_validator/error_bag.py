class ErrorBag():
    def __init__(self):
        self.errors = {}
    
    def response(self):
        if request.is_json or request.is_xhr:
            return jsonify(
                status=False,
                errors=self.errors
            ), 422
        session['errors'] = self.errors
    
    def addError(self, field, message):
        self.errors[field] = message
    
    def hasErrors(self):
        if self.errors:
            return True
        return False