def find_outlier(integers):
    even = []
    odd = []
    for item in integers:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]