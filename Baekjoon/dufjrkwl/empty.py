


def ff(x):

    i = 0
    if x<1:
        return 2
    else:
        i = (2 * ff(x-1))+1
        print(i)
        return i

ff(6)
