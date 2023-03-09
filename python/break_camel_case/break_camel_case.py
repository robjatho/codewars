def solution(s):
    words = ''
    for letter in range(0,len(s)):
        if s[letter].isupper() and letter > 0:
            words += ' ' + s[letter]
        else:
            words += s[letter]
    return words


if __name__ == '__main__':
    print(solution("breakCamelCase"))