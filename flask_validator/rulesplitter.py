def ruleSplitter(data):
    rules = data.split(':')
    rule_field = rules[0]
    if not len(rules) > 1:
       return {'rule': rule_field, 'data': []}
    return {'rule': rule_field, 'data': rules[1].split(',')}
