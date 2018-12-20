# Flask Validator

This is a validation library for flask app or api

## Installation

`pip install flask-validator`

## Example (Usage)
```
from flask import Flask, jsonify
from flask_validator import ValidatorEngine

app = Flask(__name__)
validator = ValidatorEngine(app)

@app.route('/index', methods=['POST'])
@validator('json', {
    'name': ['required', 'maxa:10']
})
def index():
    return jsonify(
        status=True
    ),200


@app.route('/users/<name>', methods=['POST'])
@validator('query_string', {
    'name': ['required', 'max:10', 'min:3']
})
def test_exp(name):
    return jsonify(
        status=True
    ),200
```

This library uses function decorator pattern, which means the incomming request data is validated before 
the request hit the route function 

### On Error
When there is a validation error, library return a 422 http response status code and a json data containing the error messages.
```
    {
        status: false,
        errors: {
            name: ["This field is required"]
        }
    }
```

### instantiating  ValidatorEngine Class
`validator = ValidatorEngine(app)`

or when use using flask factory function pattern

```
    validator = ValidatorEngine()
    validator.init_app(app)
```

###  Using the validator object
Decorate your route function with the validator object like this.
```
    @validator(<where-to-check-for-data>, <validation-logic>)
```

so you have 
```
    @validator('json', {
        'name': ['required', 'min:23']
    })
```

The first argument to the validator decorator is the place where you want the validator to check for incoming data
"json <Data coming from post request>", "query_sting<Data coming from the route url>", "headers <Incoming headers>".

The second arguement is a dictionary holding the validation rules 
```
    { <Field to validate >: [<Rules: A list if the validtion rules to check on the field sepcified> ]}
```

## Built-in Validation Rules

### `json`

Using the `json` rule, the validator expects a JSON object from the client. It validates fields in JSON data.

### `query_string`
The `query_string` rule validates the URL query arguments passed by the client.

### `headers`
Validates the request headers

## Built-in Validation Rules Args
You can specify extra argument to a rule like character limit for a parameter and required values.

### `required`
Specify a required value. 

You can require a value in a JSON payload as follows:
```
@validator('json', {
    'name': ['required', 'min:23']
})
```

### `max` and `min`
The maximum and minimum character for a parameter 
```
@validator('json', {
    'phone': ['required', 'min:8', 'max:16']
})
```

### `alpha`
This check that the input under validation contains only alphabets (A-Za-z)
```
@validator('json', {
    'name': ['alpha']
})
```

### `alphanumeric`
This check that the input under validation contains both alphabets and numbers (A-Za-z0-9)
```
@validator('json', {
    'username': ['alphanumeric']
})
```

### `list`
This check that the input under validation is a list
```
@validator('json', {
    'choice': ['list']
})
```
you can also set your validation to make sure the list is of a specific length
```
@validator('json', {
    'choice': ['list:3']
})
```
this will check test the data for list and of length 3

### 'bool'
This check that the input under validation is a boolean datatype (True/False) or (1/0)
```
@validator('json', {
    'agreed': ['bool']
})
```

### `date:<format>`
This check that the input under validation is a date that matches the `<format>` provided.
```
 @validator('json', {
    'delivery_date': ['date:%Y/%m/%d %H:%M:%S']
 })
```
The format is the standard date format codes specified in the datetime library in python
[chech it here (date formats codes)](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

### `date:<format>,<value>`
You can also validate that the date matches the format and that date value sepecified
```
@validator('json', {
    'delivery_date': ['date:%Y/%m/%d %H:%M:%S,2017/03/04 01:02:45']
})
```

### `date_before:<format>,<value>`
Checks that the date matches the format and is before the date value specified
```
@validator('json', {
    'delivery_date': ['date_before:%Y/%m/%d %H:%M:%S,2017/03/04 01:02:45']
})
```

### `date_before_or_equal:<format>,<value>`
Checks that the date matches the format and is before or equals to the date value specified
```
@validator('json', {
    'delivery_date': ['date_before_or_equal:%Y/%m/%d %H:%M:%S,2017/03/04 01:02:45']
})
```

### `date_after:<format>,<value>`
Checks that the date matches the format and is after the date value specified
```
@validator('json', {
    'delivery_date': ['date_after:%Y/%m/%d %H:%M:%S,2017/03/04 01:02:45']
})
```

### `date_after_or_equal:<format>,<value>`
Checks that the date matches the format and is after or equals to the date value specified
```
@validator('json', {
    'delivery_date': ['date_after_or_equal:%Y/%m/%d %H:%M:%S,2017/03/04 01:02:45']
})
```



## Contributions
...
## 


### Author
Created by [Adewumi Ogunbiyi](https://github.com/adekoder)
