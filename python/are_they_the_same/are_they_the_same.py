import math


def comp(array1, array2):
    if array1 and array2:

        if array1 == [] or array2 == [] or array1 == {} or array2 == {}:
            return False

        for item in array2:
            if math.sqrt(item) % 1 != 0:
                return False
            elif math.sqrt(item) not in array1 and math.sqrt(item) * -1 not in array1:
                return False

        for item in array2:
            if array2.count(item) != (array1.count(math.sqrt(item)) or array1.count(math.sqrt(item) * -1)):
                return False
        return True
    else:
        if array1 is None or array2 is None:
            return False
        if len(array1) == len(array2) == 0:
            return True
        return False
