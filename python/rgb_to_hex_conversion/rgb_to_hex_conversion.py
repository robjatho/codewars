def check_num(num):
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num


def parse(num):
    if num <= 9:
        return str(num)
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'


def rgb(r, g, b):
    r = check_num(r)
    g = check_num(g)
    b = check_num(b)
    return parse(r / 16) + parse(r % 16) + parse(g / 16) + parse(g % 16) + parse(b / 16) + parse(b % 16)
