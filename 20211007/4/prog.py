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

import sys
exec(sys.stdin.read())

