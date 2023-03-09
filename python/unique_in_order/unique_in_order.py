def unique_in_order(sequence):
    result = []
    for item in sequence:
        if item not in result:
            result.append(item)
        elif item in result and result[-1] != item:
            result.append(item)
    return result
