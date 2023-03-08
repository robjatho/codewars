def array_diff(a, b):
    check_items = []
    result = []
    for i in b:
        if a.count(i) > 0:
            check_items.append(i)
    for item in a:
        if item not in check_items:
            result.append(item)
    return result
