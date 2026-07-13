def likes(names):
    cnt = len(names)
    if cnt == 0:
        return "no one likes this"
    elif cnt == 1:
        return "{} likes this".format(names[0])
    elif cnt == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif cnt == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    elif cnt >= 4:
        return "{}, {} and {} others like this".format(names[0], names[1], cnt - 2)

print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Jacob', 'Alex', 'Mark', 'Max']))