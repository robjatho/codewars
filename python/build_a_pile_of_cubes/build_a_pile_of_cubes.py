def find_nb_slow(m):
    n=1
    end_result = 0
    while end_result <= m:
        if m - end_result == 0:
            return n
        else:
            n += 1
            end_result = n**3
            for item in range(1, n+1):
                end_result += (n-item)**3
    return -1


def find_nb(m):
    n=1
    end_result = 0
    top_result = 0
    while n > 0:
        if m - end_result == 0:
            return n
        #elif end_result > m:
        #    top_result = n
        if n > top_result:
            n = n*2
        else:
            n = n + 1
            if n == top_result:
                return -1
        end_result = n**3
        for item in reversed(range(1, n+1)):
            end_result += (n-item)**3
            if end_result > m:
                top_result = n
                n = n - item
                break
    return -1

if __name__ == '__main__':
    print(find_nb(1071225))
    print(find_nb(4183059834009))
    print(find_nb(24723578342962))