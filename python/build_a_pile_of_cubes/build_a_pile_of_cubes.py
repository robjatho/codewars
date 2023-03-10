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


if __name__ == '__main__':
    print(find_nb(1071225))
    print(find_nb(4183059834009))