from flask import Flask, jsonify
from flask_validator import ValidatorEngine

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = "This is test secret"
validator = ValidatorEngine(app)

@app.route('/index', methods=['POST'])
@validator('json', {
    'name': ['required', 'maxa:10']
})
def index():
    return jsonify(
        status=True
    ),200


@app.route('/exception', methods=['POST'])
@validator('pro', {
    'name': ['required', 'max:10', 'min:3']
})
def test_exp():
    return jsonify(
        status=True
    ),200


@app.route('/query/<name>', methods=['GET'])
@validator('query_string', {
    'name': ['required', 'max:10']
})
def query_string(name):
    return jsonify(
        status=True
    ),200


if __name__ == '__main__':
    app.run(debug=True)
