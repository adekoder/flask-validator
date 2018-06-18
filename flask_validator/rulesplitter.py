def ruleSplitter(data):
    rules = data.split(':')
    rule_field = rules[0]
    if not len(rules) > 1:
       return {'name': rule_field, 'args': []}
    return {'name': rule_field, 'args': rules[1].split(',')}
