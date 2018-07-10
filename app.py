from flask import Flask, jsonify
from flask_validator import Validator

app = Flask(__name__)
app.config['TESTING'] = True
validator = Validator(app)

@app.route('/index', methods=['POST'])
@validator('json', {
    'name': ['requireded', 'maxa:10']
})
def index():
    return jsonify(
        status=True
    ),200


@app.route('/exception', methods=['POST'])
@validator('pro', {
    'name': ['required', 'max:10']
})
def test_exp():
    return jsonify(
        status=True
    ),200




if __name__ == '__main__':
    app.run(debug=True)
