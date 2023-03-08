def valid_parentheses(string):
    if len(string) == 0:
        return True
    result = []
    for item in string:
        if item in ['(',')']:
            result.append(item)
    if result.count('(') != result.count(')'):
        return False
    print(result)
    print(len(result))
    prev = ''
    for x in result:
        prev += x
        if prev == ')' or prev.count('(') < prev.count(')'):
            return False
    return True
