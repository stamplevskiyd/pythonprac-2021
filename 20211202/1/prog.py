def decorator(fun):
    def new(*args, **kwargs):
        print("{}: {}, {}".format(fun.__name__, args[1:], kwargs))
        return fun(*args, **kwargs)
    return new


class dump(type):
    def __new__(cls, name, parents, ns):
        for elem in ns.items():
            if callable(elem[1]):
                ns[elem[0]] = decorator(elem[1])
        return super().__new__(cls, name, parents, ns)


import sys
exec(sys.stdin.read())
