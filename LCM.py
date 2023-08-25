def least_common_multiple(x, y):
    if x >y:
        greater = x
    elif y >x:
        greater = y
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break