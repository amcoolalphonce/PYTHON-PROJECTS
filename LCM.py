def least_common_multiple(x, y):
    if x >y:
        greater = x
    elif y >x:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm   

