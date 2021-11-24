def iint(typ):
    def decor(fun):
        def newf(*args):
            for arg in args:
                if type(arg) != typ:
                    raise TypeError
            res = fun(*args)
            print("<-", res)
            return res
        return newf
    return decor


@iint(int)  # проверяет, что тип аргументов - указанный
def fun(a, b):
    return a * 2 + b
