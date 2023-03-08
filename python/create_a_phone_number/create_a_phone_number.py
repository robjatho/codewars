def create_phone_number(n):
    text = ''

    for item in n:
        text += str(item)

    return '(' + text[0:3] + ') ' + text[3:6] + '-' + text[6:10]
