def duplicate_encode(word):
    word = word.lower()
    result = []
    for w in word:
        if word.count(w) > 1:
            result.append(')')
        else:
            result.append('(')
    return ''.join(result)
