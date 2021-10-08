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
s, t, u = eval(input())
value = eval(input())
F = Calc(s, t, u)
print(F(value))

