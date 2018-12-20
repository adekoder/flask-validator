from .general import General
from .date import Date

validators = {
    'required': General.required,
    'max': General.max,
    'min': General.min,
    'alpha': General.alpha,
    'alphanumeric': General.alphanumeric,
    'list': General.list,
    'bool': General.boolean,
    'date': Date.date,
    'date_after': Date.after,
    'date_after_or_equal': Date.after_or_equal
}
