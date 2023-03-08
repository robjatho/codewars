def is_valid_walk(walk):
    if len(walk) == 10:
        north = 0
        south = 0
        east = 0
        west = 0
        for item in walk:
            if item == 'n':
                north+=1
            elif item == 's':
                south+=1
            elif item == 'e':
                east+=1
            elif item == 'w':
                west+=1
        if north == south and east == west:
            return True
    return False
