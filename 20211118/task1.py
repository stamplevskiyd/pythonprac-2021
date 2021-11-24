from functools import wraps
def decor(fun):
    @wraps(fn)
    def newf(*args):
        for arg in args:
            if type(arg) != int:
                raise TypeError
        res = fun(*args)
        print("<-", res)
        return res
    return newf


@decor
def fun(a, b):
    return 2 * a + b
