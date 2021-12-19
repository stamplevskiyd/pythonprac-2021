def Calc(s: str, t: str, u: str):
    def fs(arg):
        x = arg
        return eval(s)
    def ft(arg):
        x = arg
        return eval(t)
    def fu(arg):
        x = fs(arg)
        y = ft(arg)
        return eval(u)
    return fu

from math import *
fun = Calc(*eval(input()))
print(fun(eval(input())))

