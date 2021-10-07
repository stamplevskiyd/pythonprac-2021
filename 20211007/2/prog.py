def SUB(a, b):
    if type(a) == type([]) or type(a) == type((0,)):
        res = [elem for elem in a if not elem in b]
        return tuple([elem for elem in a if not elem in b]) if type(a) == type((0,)) else [elem for elem in a if not elem in b]
    else:
        return a - b
