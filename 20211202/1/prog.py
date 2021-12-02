def decorator(fun):
    def new(*args, **kwargs):
        print(fun.__name__, args, kwargs)
        return fun(*args, **kwargs)
    return new


def dump(type):
    def __init__(self, name, parents, ns):
        for elem in ns:
            
    

class ctype(type):

    def __call__(self, *args, **kwargs):
        print("call", self, args, kwargs)
        return super().__call__(*args, **kwargs)

    def __new__(cls, name, parents, ns):
        print("new", cls, name, parents, ns)
        return super().__new__(cls, name, parents, ns)

    def __init__(self, name, parents, ns):
        print("init", self, parents, ns)
        return super().__init__(name, parents, ns)

class C(int, metaclass=ctype):
     field = 42

c = C("100500", base=16)
